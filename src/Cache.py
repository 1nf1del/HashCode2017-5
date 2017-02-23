class Cache():

    def __init__(self, id=0, taille=0, tailleMax=0):
    """ Constrcuteur de la classe Cache"""
        self.id = id
        self.taille = taille
        self.tailleMax = tailleMax
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
        self.videos.append(video)