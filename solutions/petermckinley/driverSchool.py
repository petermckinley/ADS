class School:
    def __init__(self):
        self.allStudents = {} #student : instructor
        self.instructors = [] #all instructor objects

    def puntuacion(self, student):#o(1) dictionary lookup
        #find student instructor, then find score in instructor book
        if (instructor := self.allStudents.get(student)) is not None:
            return instructor.students[student]
        return "Error"

    def alta(self, student, instruct_name):#overall o(n)
    # Check if student exists, if yes, switch them to a new instructor, else register
        instructor = None
        for people in self.instructors:#o(n)
            if instruct_name == people.firstName:
                instructor = people
                break
        
        if instructor is None:
            instructor = Instructor(instruct_name)
            self.instructors.append(instructor)

        temp_points = 0
        if student in self.allStudents:
            current_instructor = self.allStudents[student]
            if current_instructor != instructor:
                temp_points = current_instructor.students.get(student)
                current_instructor.students.pop(student, None)
            else:
                return

        self.allStudents[student] = instructor
        instructor.students[student] = temp_points 
        
    def es_alumno(self, student, instrutor_name):#dict lookup o(1)
        #checks if registered under instructor
        if student in self.allStudents:
            instructor = self.allStudents[student]
            if instructor.firstName == instrutor_name:
                if student in instructor.students:
                    return f"{student} es alumno de {instrutor_name}"
        return f"{student} no es alumno de {instrutor_name}"
    
    def actualizar(self, student, points):#o(1) dict stuff
        #adds points to student if exists
        if self.allStudents.get(student) is not None:
            instructor = self.allStudents[student]
            instructor.students[student] += int(points)
            return
        return f"El alumno {student} no esta matriculado."
    
    def examen(self, instructor, points):#o(number of instructors + numStudents log numstudents)
        #call instructor funciton, using their list
        #alphabeticlly sort, returns list to be printed by text reader
        instructorobj = None
        for people in self.instructors:
            if instructor == people.firstName:
                instructorobj = people
                break
        
        if isinstance(instructorobj, str):
            return []
        if instructorobj is None:
            return []

        temp_list = []
        for students in instructorobj.students:
            if instructorobj.students[students] >= int(points):
                temp_list.append(students)
        temp_list.sort()
        return temp_list
    
    def aprobar(self, student):#o(1)
        #find instructor, delete from them, then delete from school
        if (instructor := self.allStudents.get(student)) is not None:
            instructor.students.pop(student)
        self.allStudents.pop(student)
        return

class Student:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.address = ""
    
    def setInfo(self, fn, ln, add):
        self.firstName = fn
        self.lastName = ln
        self.address = add

class Instructor:
    def __init__(self, name):
        self.firstName = name
        self.lastName = ""
        self.address = ""
        self.students = {}#student, points

    def setInfo(self, fn, ln, add):
        self.firstName = fn
        self.lastName = ln
        self.address = add
    

def process_input():#time not applicable
    school = School()
    output = []
    while True:
        command = input().strip()
        parts = command.split()
        op = parts[0]

        if op == "alta":
            output.append(school.alta(parts[1], parts[2]))
        elif op == "puntuacion":
            result = school.puntuacion(parts[1])
            if result == "Error":
                output.append(f"El alumno {parts[1]} no esta matriculado")
            else:
                output.append(f"Puntuacion de {parts[1]}: {result}")
        elif op == "es_alumno":
            output.append(school.es_alumno(parts[1], parts[2]))
        elif op == "actualizar":
            output.append(school.actualizar(parts[1], parts[2]))
        elif op == "examen":
            temp = school.examen(parts[1], parts[2])
            output.append(f"Alumnos de {parts[1]} a examen:")
            for people in temp:
                output.append(people)
        elif op == "aprobar":
            output.append(school.aprobar(parts[1]))
        elif op == "FIN":
            output.append("---")
            break
        else:
            output.append("ERROR: Comando no valido\n")
    
    for line in output:
        if line != None:
            print(line)

process_input()

        #add command read
