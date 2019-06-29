import socket
import ssl
import SSLMessage as sslCommand
from SSLMessageEncoder import  SSLMessageEncoder as MyEncoder
import json

def sendMessage(line1,line2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Require a certificate from the server.  We used a self-signed
        # certificate
        # so here ca_certs must be the server certificate itself.
        ssl_sock = ssl.wrap_socket(s,
                                   ca_certs="server.crt",
                                   cert_reqs=ssl.CERT_REQUIRED)
        
        ssl_sock.connect(('localhost', 10023))
        params = dict()
        params['line1'] = line1
        params['line2'] =line2
        cmd = sslCommand.SSLMessage('displayMessage',params)
        converted = serialize(cmd)
        ssl_sock.write(converted.encode('utf-8'))

def readTemp():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Require a certificate from the server.  We used a self-signed
        # certificate
        # so here ca_certs must be the server certificate itself.
        ssl_sock = ssl.wrap_socket(s,
                                   ca_certs="server.crt",
                                   cert_reqs=ssl.CERT_REQUIRED)
        
        ssl_sock.connect(('localhost', 10023))
        params = dict()
        params['line1'] = 'sei tu'
        params['line2'] ='fantasticoguerriero'
        cmd = sslCommand.SSLMessage('displayMessage',params)
        converted = serialize(cmd)
        ssl_sock.write(converted.encode('utf-8'))

def serialize(self):    
    serialized = json.dumps(MyEncoder().encode(self),cls=MyEncoder)
    return serialized 


if __name__ == '__main__':
    openSocket()