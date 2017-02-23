class Endpoint():
	
	def __init__(self, ld, cacheServers):
		# self.ld      = Latence du Data Center vers l'Endpoint
		# cacheServers = Listes des cacheServers connectés à l'Endpoint | format : Map < idCacheServer, Latence >
		self.ld = ld
		self.cacheServers = cacheServers

	def chooseCacheServer(self, video):
		pass

	def sortCache(self):
		return self.cacheServers.sort()
