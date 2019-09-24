import feedparser
import MessageConsumer
import threading
import time
class RssReader(object):
    MessageConsumerIstance = MessageConsumer.MessageConsumer()
    SourceList = ['']
    SleepIntervalSecond = 300

    def __init__(self,MessageConsumer,sourceList,interval=1):
        self.MessageConsumerIstance = MessageConsumer
        self.SourceList=sourceList
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            try:
                print('readRSS')
                for address in self.SourceList:
                    feed = feedparser.parse(address)
                    for post in feed.entries:
                      date = "(%d/%02d/%02d)" % (post.published_parsed.tm_mday , post.published_parsed.tm_mon, post.published_parsed.tm_year)            
                      self.MessageConsumerIstance.AddRssMessage(date,post.title)
                time.sleep(self.SleepIntervalSecond)
            except Exception as e:
                print(e)
                    