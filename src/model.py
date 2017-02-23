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
            caches.append(Cache(i, cacheCapacity))

        # Videos line
        videoSizes = f.readline().split(" ")
        self.videos = []
        for i in range(videoCount):
            self.videos.append(Video(i, videoSizes[i]))

        # Endpoints section
        self.endpoints = []
        for i in range(endpointCount):
            endpointLine = f.readline().split(" ")
            latency = int(endpointLine[0])
            availableCacheCount = int(endpointLine[1])
            caches = {}
            for j in range(availableCacheCount):
                cacheLine = f.readline().split(" ")
                caches[int(cacheLine[0])] = int(cacheLine[1])
            self.endpoints.append(Endpoint(latency, caches))

        # Requests section
        self.requests = []
        for i in range(requestCount):
            requestLine = f.readline().split(" ")
            requests.append(Request(self.videos[int(requestLine[0])],int(requestLine),endpoints[int(requestLine[1])]))

