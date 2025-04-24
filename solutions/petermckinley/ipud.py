from collections import deque, OrderedDict

class iPud:
    def __init__(self):
        self.trackList = {}  #{song_name: (artist, duration)}
        self.songQueue = deque()  # Queue for playback
        self.historyDict = OrderedDict()  
        self.totalDuration = 0  # duration of  playlist
    
    # O(1) dictionary insertion
    def addSong(self, title, musician, length):
        if title in self.trackList:
            return "ERROR addSong"
        self.trackList[title] = (musician, int(length))
        return None
    
    # O(1) appends if not present
    def addToPlaylist(self, track):
        if track not in self.trackList:
            return "ERROR addToPlaylist"
        if track not in self.songQueue:
            self.songQueue.append(track)
            self.totalDuration += self.trackList[track][1]
        return None
    
    # O(1)  first element
    def currentSong(self):
        if not self.songQueue:
            return "ERROR current"
        return self.songQueue[0]
    
    # O(1) from front 
    def play(self):
        if not self.songQueue:
            return "No hay canciones en la lista"
        song = self.songQueue.popleft()
        self.totalDuration -= self.trackList[song][1]
        if song in self.historyDict:
            del self.historyDict[song]
        self.historyDict[song] = None  # Preserve order
        return f"Sonando {song}"
    
    # O(1)Returns stored total duration
    def total_time(self):
        return f"Tiempo total {self.totalDuration}"
    
    # O(N) - Slices list up to N
    def recentSongs(self, count):
        recent_songs = list(self.historyDict.keys())[-count:][::-1]
        if not recent_songs:
            return "No hay canciones recientes"
        output = [f"Las {len(recent_songs)} mas recientes"]
        output.extend(f"    {song}" for song in recent_songs)
        return output
    
    # O(1) - Removing from dicts and queue
    def delete_song(self, title):
        if title in self.trackList:
            del self.trackList[title]
        if title in self.songQueue:
            self.songQueue.remove(title)
            self.totalDuration -= self.trackList[title][1]
        if title in self.historyDict:
            del self.historyDict[title]
        return None

def process_input():
    ipudPlayer = iPud()
    outputLog = []
    while True:
        command = input().strip()
        args = command.split()
        action = args[0]

        if action == "addSong":
            response = ipudPlayer.addSong(args[1], args[2], args[3])
            if response:
                outputLog.append(response)
        elif action == "addToPlaylist":
            response = ipudPlayer.addToPlaylist(args[1])
            if response:
                outputLog.append(response)
        elif action == "current":
            response = ipudPlayer.currentSong()
            if response:
                outputLog.append(response)
        elif action == "play":
            outputLog.append(ipudPlayer.play())
        elif action == "totalTime":
            outputLog.append(ipudPlayer.total_time())
        elif action == "recent":
            response = ipudPlayer.recentSongs(int(args[1]))
            if isinstance(response, list):
                outputLog.extend(response)
            else:
                outputLog.append(response)
        elif action == "deleteSong":
            ipudPlayer.delete_song(args[1])
        elif action == "FIN":
            outputLog.append("---")
            break
        else:
            outputLog.append("ERROR: Comando no valido\n")
    
    for line in outputLog:
        if line is not None:
            print(line)

process_input()
