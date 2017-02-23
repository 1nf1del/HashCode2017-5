class Cache():

    def __init__(self, id=0, capacity=0):
        """ Constrcuteur de la classe Cache """
        self.id = id
        self.freeSpace = capacity
        self.capacity = capacity
        self.videos = []

    def __str__(self):
        """ Retourne le string au format attendu :
        id v1 v2 ... vn
        """
        res = "{self.id}"
        for video in videos:
            res += " " + video.id
        return res

    def addVideo(self, video):
        if self.hasEnoughSpace(video.size):
            self.videos.append(video)
            self.freeSpace = self.freeSpace - video.size

    def removeVideo(self, video):
        self.videos.remove(video)
        self.freeSpace = self.freeSpace + video.size

    def hasEnoughSpace(self, size):
        return True if (self.freeSpace >= size) else False
