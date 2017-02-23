class Endpoint():
	
	def __init__(self, Ld, Req, cacheServers):
		self.Ld = Ld
		self.Req = Req
		self.cacheServers = cacheServers

	def chooseCacheServer(self, video):
		pass

	def sortCache(self):
		return self.cacheServers.sort()
