#from SSLMessageEncoder import SSLMessageEncoder as MyEncoder
import json
class SSLMessage(object):
    """description of class"""
    command = ""
    parameters = dict()

    def __init__(self,command,parameters):
        self.command = command
        self.parameters = parameters



#def serialize(self):    
#    serialized = json.dumps(MyEncoder().encode(self),cls=MyEncoder)
#    return serialized 
#
#def deserialize(serializedString):
#    sslMessage = json.loads(data, object_hook = command.as_sslMessage)
