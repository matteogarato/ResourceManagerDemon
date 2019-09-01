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
import feedparser


MessageQueue = []
RssMessage = []
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
        print('enter readTemperature')
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
    elif len(MessageQueue) == 0 and not(ScreenInstance.display) and len(RssMessage) > 0:
         toShow = 0
         for val in RssMessage:
             if val.displayed == True:
                 toShow+=1
         print("displaing: {}".format(RssMessage[toShow].line2))
         ScreenInstance.textmessagerecieved(RssMessage[toShow].line1,RssMessage[toShow].line2)
         RssMessage[toShow].displayed = True


def readRSS():
    print('readRSS')
    feed = feedparser.parse("https://news.ycombinator.com/rss")
    for post in feed.entries:
      date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year, post.published_parsed.tm_mon, post.published_parsed.tm_mday)
      msgtoprint = msg.Message(date,post.title)
      for val in RssMessage:
        if msgtoprint.line2!=val.line2:
            print("added: {}".format(post.title))
            RssMessage.append(msgtoprint)


def main():
    readRSS()
    bindsocket = socket.socket()
    bindsocket.bind(('', 10023))
    bindsocket.listen(5)
    while True:
        print("messageQueueRemover")
        messageQueueRemover()
        print("readRSS")
        readRSS()
        print("readMessage")
        readMessage(bindsocket)

#run the daemon calling main
#with daemon.DaemonContext():
if __name__ == '__main__':
    main()