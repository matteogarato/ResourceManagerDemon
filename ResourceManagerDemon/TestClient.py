import Client

if __name__ is '__main__':
    clientInstance = Client.Client("192.168.3.XX")
    readed=clientInstance.readTemp()
    print(readed)