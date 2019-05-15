from json import JSONEncoder
from SSLMessage import SSLMessage as message

class SSLMessageEncoder(JSONEncoder):    
    def default(self, z):
        if isinstance(z,message):
             return (z.command, z.parameters)
        else:
             return super().default(z) 

