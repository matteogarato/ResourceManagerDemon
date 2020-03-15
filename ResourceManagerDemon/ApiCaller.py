import requests
class ApiCaller(object):
    """necessary methods to semplify api call"""
    baseUrl=""

    def __init__(self, baseUrlFromCaller):
        self.baseUrl = baseUrlFromCaller        

    def callPlateVerificationApi(readedCode):
        url = self.baseUrl + '/PlateVerification/' + readedCode
        response = requests.post(url,'')
        return response

    def callCardVerificationApi(readedCode):
        url = self.baseUrl + '/CardVerification/' + readedCode
        response = requests.post(url,'')
        return response
