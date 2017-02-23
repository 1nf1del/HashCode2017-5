class Request():
	
	def __init__(self, video, nbReq, endpoint):
		# self.video    = id de la video concernee
		# self.nbReq    = nombre de requetes venant de l'endpoint sur la video
		# self.ratio    = nombre de requetes / taille de la video
		# self.endpoint = endpoint d'ou proviennent les requetes
		self.video = video
		self.nbReq = nbReq
		self.ratio = 0
		self.endpoint = endpoint

	def calcRatio(self):
		self.ratio = self.nbReq / self.video.size
		pass
		
