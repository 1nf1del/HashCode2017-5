class Request():
	
	def __init__(self, video, nbReq, endpoint):
		# self.video    = id de la video concernée
		# self.nbReq    = nombre de requêtes venant de l'endpoint sur la video
		# self.ratio    = nombre de requêtes / taille de la video
		# self.endpoint = endpoint d'où proviennent les requêtes
		self.video = video
		self.nbReq = nbReq
		self.ratio = 0
		self.endpoint = endpoint

	def calcRatio(self):
		self.ratio = self.nbReq / self.video.size
		pass
		