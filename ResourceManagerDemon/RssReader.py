import feedparser
import MessageConsumer
import threading
class RssReader(object):
    def readRSS():
        print('readRSS')
        feed = feedparser.parse("https://news.ycombinator.com/rss")
        for post in feed.entries:
          date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year, post.published_parsed.tm_mon, post.published_parsed.tm_mday)            
          MessageConsumer.MessageConsumer.AddRssMessage(date,post.title)