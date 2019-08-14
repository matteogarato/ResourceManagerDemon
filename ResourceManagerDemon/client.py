class Client(object):
    import socket
    import ssl
    import SSLMessage as sslCommand
    from SSLMessageEncoder import  SSLMessageEncoder as MyEncoder
    import json
    
    def sendMessage(line1,line2):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = ssl.wrap_socket(s,
                                       ca_certs="server.crt",
                                       cert_reqs=ssl.CERT_REQUIRED)
            
            ssl_sock.connect(('192.168.71.142', 10023))
            params = dict()
            params['line1'] = line1
            params['line2'] =line2
            cmd = sslCommand.SSLMessage('displayMessage',params)
            converted = serialize(cmd)
            ssl_sock.write(converted.encode('utf-8'))
            ssl_sock.close()
    
    def readTemp():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = ssl.wrap_socket(s,
                                       ca_certs="server.crt",
                                       cert_reqs=ssl.CERT_REQUIRED)
            
            ssl_sock.connect(('192.168.71.142', 10023))
            params = dict()
            cmd = sslCommand.SSLMessage('displayMessage',params)
            converted = serialize(cmd)
            ssl_sock.write(converted.encode('utf-8'))
            data = ssl_sock.read()
            ssl_sock.close()
    
    def serialize(self):    
        serialized = json.dumps(MyEncoder().encode(self),cls=MyEncoder)
        return serialized 
    