from json import JSONEncoder

class SSLMessageEncoder(JSONEncoder):    
    def default(self, o):
                return o.__dict__ 

