import feedparser
import MessageConsumer
import threading
import time
class RssReader(object):
    MessageConsumerIstance = MessageConsumer.MessageConsumer()
    SourceList = ['']

    def __init__(self,MessageConsumer,sourceList,interval=1):
        self.interval = interval
        self.MessageConsumerIstance = MessageConsumer
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        try:
            while True:
                print('readRSS')
                for address in SouceList:
                    feed = feedparser.parse(address)#todo: config file
                    for post in feed.entries:
                      date = "(%d/%02d/%02d)" % (post.published_parsed.tm_mday , post.published_parsed.tm_mon, post.published_parsed.tm_year)            
                      self.MessageConsumerIstance.AddRssMessage(date,post.title)
                time.sleep(300)
        except Exception as e:
                print(e)
                #todo error managemant aka thread restart