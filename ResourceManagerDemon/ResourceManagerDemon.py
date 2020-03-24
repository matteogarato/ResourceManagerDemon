import socket
import ssl
import configparser
import TempReading
from SSLMessage import SSLMessage as command
import SSLMessage as SSLMessageStatic
import json
import MessageConsumer
import RssReader
import ApiCaller
#import ptvsd
#ptvsd.enable_attach()

MessageConsumerIstance = MessageConsumer.MessageConsumer()
ApiCallerInstance = ApiCaller.ApiCaller("")
configParser = configparser.RawConfigParser()
configFilePath = r'ResourceManagerDemon.Config'

def readMessage(bindsocket):
    print('readMessage')
    newsocket, fromaddr = bindsocket.accept()
    print('newsocket')
    connstream = ssl.wrap_socket(newsocket,
                             server_side=True,
                             certfile="server.crt",#todo: config file
                             keyfile="server.key")#todo: config file
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


def displayMessage(parametersdict):
    try:
        print('enter displayMessage')
        MessageConsumerIstance.AddMessage(parametersdict['line1'],parametersdict['line2'])
        print('exit from displayMessage')
        return b'OK'
    except Exception as e:
        return e.args

def readTemperature(parametersdict):
    try:
        hum,temp = TempReading.TempReading()
        print('exit from readTemperature')
        print('T:{};H:{}'.format(temp,hum))
        return b'T:{};H:{}'.format(temp,hum)
    except Exception as e:
        return e.args

def verifyCode(parametersdict):
    try:
        result = ApiCaller.ApiCaller.callPlateVerificationApi(parametersdict['Code'])
        print('exit from readTemperature')
        print('T:{};H:{}'.format(temp,hum))
        return b'T:{};H:{}'.format(temp,hum)
    except Exception as e:
        return e.args


def main():
    print('Read Configuration')
    configParser.read(configFilePath)
    addressList = configParser.get('RSSCONFIG', 'urls').split(',')
    portReading = int(configParser.get('SSLCONFIG', 'port'))
    print('RssReaderIstance')
    RssReaderIstance = RssReader.RssReader(MessageConsumerIstance,addressList)
    ApiCallerInstance = ApiCaller.ApiCaller(configParser.get('API', 'BaseUrl'))
    bindsocket = socket.socket()
    bindsocket.bind(('', portReading))
    bindsocket.listen(5)
    while True:
        try:
            readMessage(bindsocket)
        except Exception as e:
                print(e)
                #todo error managemant aka thread restart
if __name__ == '__main__':
    main()