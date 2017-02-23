def first_algo():
	"first algorithm"
	Model.sortC()
	for endpoint in Model.endpoints :
		for request in endpoint.request :
			request.calcRatio()
	Model.sortrequest()
	for request in Model.requests :
		vid=request.video
		request.endpoint.chooseCache(video)
	finalString = ""
	for cache in Model.caches :
		finalString = finalString + cache.toString() + "\n" 
	return finalString