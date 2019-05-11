import socket
import ssl
import SSLMessage as sslCommand
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server.  We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('localhost', 10023))
params = []
cmd = sslCommand.SSLMessage()
cmd.command = 'KEN'
cmd.parameters = params
converted = sslCommand.serialize(cmd)
print (converted)
ssl_sock.write(converted.encode())
print(ssl_sock.getpeername())
print(ssl_sock.cipher())
print(ssl_sock.getpeercert())


if False: # from the Python 2.7.3 docs
    # Set a simple HTTP request -- use httplib in actual code.
    ssl_sock.write("""GET / HTTP/1.0r
    Host: www.verisign.comnn""")

    # Read a chunk of data.  Will not necessarily
    # read all the data returned by the server.
    data = ssl_sock.read()

    # note that closing the SSLSocket will also close the underlying socket
    ssl_sock.close()
