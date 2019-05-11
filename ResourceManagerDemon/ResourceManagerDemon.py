import socket
import ssl
#import daemon
import configparser
#import Screen
import Message as msg
import SSLMessage as command
import json




MessageQueue = []

def readMessage(bindsocket):
    newsocket, fromaddr = bindsocket.accept()
    print('newsocket')
    connstream = ssl.wrap_socket(newsocket,
                             server_side=True,
                             certfile="server.crt",
                             keyfile="server.key")
    print('connstream')
    #try:
    clientMessageDispatcher(connstream)
    #finally:
        #connstream.shutdown(socket.SHUT_RDWR)
        #connstream.close()
def clientMessageDispatcher(connstream):
    try:
        print('clientMessageDispatcher')
        data = connstream.read()    
        print('data: {}'.format(data))
        sslMessage = json.loads(data, object_hook = command.as_sslMessage)
    except:
        main()




def readConfig():
    configParser = configparser.RawConfigParser()
    configFilePath = r'ResourceDemon.config'
    configParser.read(configFilePath)


def displayMessage(line1,line2):
    MessageQueue.append(msg(line1,line2))


def messageQueueRemover():
    if len(MessageQueue) > 0 and not(Screen.display):
        messageTodisplay = msg(MessageQueue[0])
        #Screen.textmessagerecieved(messageTodisplay.line1,messageTodisplay.line2)
        MessageQueue.pop(0)

def main():
    bindsocket = socket.socket()
    bindsocket.bind(('', 10023))
    bindsocket.listen(5)
    while True:
        readMessage(bindsocket)
        messageQueueRemover()

#run the daemon calling main
#with daemon.DaemonContext():
if __name__ == '__main__':
    main()