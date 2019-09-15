import Message as msg
import threading
import Screen
class MessageConsumer(object):
    MessageQueue = []
    RssMessage = []
    ScreenInstance = Screen.Screen()

    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while true:
            messageQueueRemover()

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


    def AddMessage(line1, line2):        
        MessageQueue.append(msg.Message(line1,lin2))

    def AddRssMessage(line1,line2):
         msgtoprint = msg.Message(line1,line2)
         if len(RssMessage) > 0:
                found = False
                for val in RssMessage:
                  if msgtoprint.line2 == val.line2:
                      found = True
                if found == False:
                 print("added: {}".format(post.title))
                 RssMessage.append(msgtoprint)
         else:
                RssMessage.append(msgtoprint)