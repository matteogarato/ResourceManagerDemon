import client

if __name__ is '__main__':
    clientInstance = client.Client()
    readed=clientInstance.readTemp()
    print(readed)