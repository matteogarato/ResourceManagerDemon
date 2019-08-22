import client

if __name__ == '__main__':
    clientInstance = client.Client()
    readed=clientInstance.readTemp()
    print(readed)