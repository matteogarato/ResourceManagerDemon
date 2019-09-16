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

    def messageQueueRemover(self):
        print('Display message')
        if len(self.MessageQueue) > 0 and not(ScreenInstance.display):
            print('line1:{} line2:{}'.format(self.MessageQueue[0].line1,self.MessageQueue[0].line2))
            ScreenInstance.textmessagerecieved(self.MessageQueue[0].line1,self.MessageQueue[0].line2)
            self.MessageQueue.pop(0)
        elif len(self.MessageQueue) == 0 and not(ScreenInstance.display) and len(self.RssMessage) > 0:
             toShow = 0
             for val in self.RssMessage:
                 if val.displayed == True:
                     toShow+=1
             print("displaing: {}".format(self.RssMessage[toShow].line2))
             ScreenInstance.textmessagerecieved(self.RssMessage[toShow].line1,self.RssMessage[toShow].line2)
             self.RssMessage[toShow].displayed = True


    def AddMessage(line1, line2):        
        self.MessageQueue.append(msg.Message(line1,lin2))

    def AddRssMessage(line1,line2):
         msgtoprint = msg.Message(line1,line2)
         if len(self.RssMessage) > 0:
                found = False
                for val in self.RssMessage:
                  if msgtoprint.line2 == val.line2:
                      found = True
                if found == False:
                 print("added: {}".format(post.title))
                 self.RssMessage.append(msgtoprint)
         else:
                self.RssMessage.append(msgtoprint)