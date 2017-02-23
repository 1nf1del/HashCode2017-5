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
    finalString = ""
    for cache in model.caches:
        finalString = finalString + str(cache) + "\n" 
    return finalString

