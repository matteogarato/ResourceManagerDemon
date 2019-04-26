import socket
import ssl
import daemon
import configparser
import Screen
import Message

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')



MessageQueue = [Message()]

def readMessage(conn):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(('127.0.0.1', 8443))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()


def readConfig():
    configParser = configparser.RawConfigParser()
    configFilePath = r'ResourceDemon.config'
    configParser.read(configFilePath)

def sendMessage():
    from multiprocessing.connection import Client
    address = ('localhost', 6000)
    conn = Client(address, authkey='secret password')
    conn.send('close')
    # can also send arbitrary objects:
    # conn.send(['a', 2.5, None, int, sum])
    conn.close()

def displayMessage(line1,line2):
    MessageQueue.append(Message(line1,line2))


def messageQueueRemover():
    if len(MessageQueue) > 0 and not(Screen.display):
        messageTodisplay = MessageQueue[0]
        Screen.textmessagerecieved(messageTodisplay.line1,messageTodisplay.line2)


def main():
    address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
    listener = Listener(address, authkey='secret password')
    conn = listener.accept()
    print('connection accepted from', listener.last_accepted)
    while True:
       readMessage(conn)
       messageQueueRemover()

#run the daemon calling main
with daemon.DaemonContext():
    main()