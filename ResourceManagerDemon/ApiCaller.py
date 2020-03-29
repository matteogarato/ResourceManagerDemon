import requests
class ApiCaller(object):
    """necessary methods to semplify api call"""
    baseUrl = ""

    def __init__(self, baseUrlFromCaller):
        self.baseUrl = baseUrlFromCaller        

    def codeVerificationApi(readedCode):
        url = self.baseUrl + readedCode
        response = requests.post(url,'')
        return response
    
    def deserializeResponse(response):
        ##TODO: convert the response and generate a message to be dispayed
        response
