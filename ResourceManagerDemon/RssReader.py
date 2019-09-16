import feedparser
import MessageConsumer
import threading
class RssReader(object):
    MessageConsumerIstance = MessageConsumer.MessageConsumer()

    def __init__(self,MessageConsumer ,interval=1):
        self.interval = interval
        self.MessageConsumerIstance = MessageConsumer
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while true:
           readRSS()
           time.sleep(300)

    def readRSS():
        print('readRSS')
        feed = feedparser.parse("https://news.ycombinator.com/rss")
        for post in feed.entries:
          date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year, post.published_parsed.tm_mon, post.published_parsed.tm_mday)            
          self.MessageConsumerIstance.AddRssMessage(date,post.title)