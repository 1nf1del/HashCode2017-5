from endpoint import Endpoint
from video import Video
from request import Request
from cache import Cache

class Model():

    def __init__(self, f):
        # First line
        params = f.readline().split(" ")
        videoCount = int(params[0])
        endpointCount = int(params[1])
        requestCount = int(params[2])
        cacheCount = int(params[3])
        cacheCapacity = int(params[4])

        # Chaches
        self.caches = []
        for i in range(cacheCount):
            self.caches.append(Cache(i, cacheCapacity))

        # Videos line
        videoSizes = f.readline().split(" ")
        self.videos = []
        for i in range(videoCount):
            self.videos.append(Video(i, int(videoSizes[i])))

        # Endpoints section
        self.endpoints = []
        for i in range(endpointCount):
            endpointLine = f.readline().split(" ")
            latency = int(endpointLine[0])
            availableCacheCount = int(endpointLine[1])
            caches = []
            for j in range(availableCacheCount):
                cacheLine = f.readline().split(" ")
                cacheTuple = (self.caches[int(cacheLine[0])], int(cacheLine[1]))
                caches.append(cacheTuple)
            self.endpoints.append(Endpoint(latency, caches))

        # Requests section
        self.requests = []
        for i in range(requestCount):
            requestLine = f.readline().split(" ")
            videoId = int(requestLine[0])
            endpointId = int(requestLine[1])
            requestCount = int(requestLine[2])
            request = Request(self.videos[videoId],self.endpoints[endpointId],requestCount)
            self.requests.append(request)
            self.endpoints[endpointId].requests.append(request)

    def sortRequests(self):
        def sortByRatio(x, y, attr=ratio):
            return cmp(getattr(x, attr), getattr(y, attr))
        self.requests.sort(sortByRatio)

    def score(self):
        pass
