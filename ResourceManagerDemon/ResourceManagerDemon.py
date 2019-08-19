import socket
import ssl
import daemon
import configparser
import Screen
import TempReading
import Message as msg
from SSLMessage import SSLMessage as command
import SSLMessage as SSLMessageStatic
import json


MessageQueue = []
TempReadingInstance = TempReading.TempReading()
ScreenInstance = Screen.Screen()

def readMessage(bindsocket):
    newsocket, fromaddr = bindsocket.accept()
    print('newsocket')
    connstream = ssl.wrap_socket(newsocket,
                             server_side=True,
                             certfile="server.crt",
                             keyfile="server.key")
    print('connstream')
    try:
        clientMessageDispatcher(connstream)
    finally:       
        connstream.close()
def clientMessageDispatcher(connstream):
    try:
        print('clientMessageDispatcher')
        data = connstream.read() 
        print('data:{}'.format(data))
        data = data.decode('utf-8')
        print('decoded:{}'.format(data))
        data = json.loads(data)
        recived = json.loads(data, object_hook = as_sslMessage)
        sslMessage = command(recived[0],recived[1])
        commandRecived = sslMessage.command
        result = globals()[sslMessage.command](sslMessage.parameters)
        connstream.write(result)
    except Exception as e:
        print(e)
        main()

def as_sslMessage(dct):
    if '__SSLMessage__' in dct:
        return command(dct['command'], dct['parameters'])
    return dct


def readConfig():
    configParser = configparser.RawConfigParser()
    configFilePath = r'ResourceDemon.config'
    configParser.read(configFilePath)


def displayMessage(parametersdict):
    try:
        print('enter displayMessage')
        msgtoprint = msg.Message(parametersdict['line1'],parametersdict['line2'])
        MessageQueue.append(msgtoprint)
        print('exit from displayMessage')
        return b'OK'
    except Exception as e:
        return e.args

def readTemperature(parametersdict):
    try:
        temp = TempReadingInstance.getTemperature()
        hum = TempReadingInstance.getHumidity()
        print('exit from readTemperature')
        print('T:{};H:{}'.format(temp,hum))
        return b'T:{};H:{}'.format(temp,hum)
    except Exception as e:
        return e.args


def messageQueueRemover():
    print('Display message')
    if len(MessageQueue) > 0 and not(ScreenInstance.display):
        print('line1:{} line2:{}'.format(MessageQueue[0].line1,MessageQueue[0].line2))
        ScreenInstance.textmessagerecieved(MessageQueue[0].line1,MessageQueue[0].line2)
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