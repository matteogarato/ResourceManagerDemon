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
        try:
            while True:
                    print('Display message')
                    if self.MessageQueue and not(self.ScreenInstance.display):
                        print('line1:{} line2:{}'.format(self.MessageQueue[0].line1,self.MessageQueue[0].line2))
                        self.ScreenInstance.textmessagerecieved(self.MessageQueue[0].line1,self.MessageQueue[0].line2)
                        self.MessageQueue.pop(0)
                    elif not(self.MessageQueue) and not(self.ScreenInstance.display) and self.RssMessage:#todo: add a config to turn off rss display
                         toShow = 0
                         for val in self.RssMessage:
                             if val.displayed is True:
                                 toShow+=1
                         print("displaing: {}".format(self.RssMessage[toShow].line2))
                         self.ScreenInstance.textmessagerecieved(self.RssMessage[toShow].line1,self.RssMessage[toShow].line2)
                         self.RssMessage[toShow].displayed = True
        except Exception as e:
                print(e)
                #todo error managemant aka thread restart

    def AddMessage(self,line1, line2):        
        self.MessageQueue.append(msg.Message(line1,lin2))

    def AddRssMessage(self,line1,line2):
         msgtoprint = msg.Message(line1,line2)
         if self.RssMessage:
                found = False
                for val in self.RssMessage:
                  if msgtoprint.line2 is val.line2:
                      found = True
                if found is False:
                 print("added: {}".format(line2))
                 self.RssMessage.append(msgtoprint)
         else:
                self.RssMessage.append(msgtoprint)