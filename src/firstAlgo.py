from model import Model

def firstAlgo(model):
    "first algorithm"
    for endpoint in model.endpoints:
        endpoint.sortCaches()
        for request in endpoint.requests:
            request.getRatio()
        model.sortRequests()
    for request in model.requests:
        vid = request.video
        request.endpoint.chooseCache(vid)
    for cache in model.caches:
        for video in model.videos:
            if (video not in cache.videos):
                cache.addVideo(video)
    finalString = ""
    finalString = finalString + str(len(model.caches)) + "\n"
    for cache in model.caches:
        finalString = finalString + str(cache) + "\n"
    return finalString
