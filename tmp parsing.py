import requests  # , time, xml
from bs4 import BeautifulSoup
import datetime as dt
import feedparser

def parsing_news(url):
    i = 0
    # udm_news = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    feeds = feedparser.parse(url)

    working_date = dt.datetime.today() - dt.timedelta(7)
    i = 1
    for feed in feeds.entries:
        datetime_object = dt.datetime.strptime(str(feed.published).rstrip(" GMT"),  '%a, %d %b %Y %H:%M:%S')
        published_date = dt.datetime.today().strftime('%a, %d %B %Y %H:%M:%S')
        if datetime_object < working_date:
            break
        i += 1
    for title in soup.find_all('description')[:i]:
        print(str(title.text).split('https://www.kommersant.ru')[0])
    # print(i)
        # print(feed.summary)
    # print(soup)



if __name__ == '__main__':
    parsing_news("https://rsshub.app/telegram/channel/udmurt_gov")