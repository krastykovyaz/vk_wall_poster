import requests  # , time, xml
from bs4 import BeautifulSoup
import datetime as dt
import re, feedparser


def fix_string(text, k):
    text = text.strip()
    pattern = r'[a-z][A-Z]|\d[A-Z]|[а-я][А-Я]|[а-я][a-z]|\d[a-z]|\d[а-я]|[а-я][A-Z]|[a-z][а-я]'
    result_find = re.findall(pattern, text)
    for match in result_find:
        text = text.replace(match, ' '.join(match))
    if 'https://www.kommersant.ru' in text and 'Коммерсант' in k:
        text = text.split('https://www.kommersant.ru')[0]
    if text.startswith('Темная Удмуртия:'):
        text = text.lstrip('Темная Удмуртия:')
    text = text.strip()
    return text

def feeding_date(url):
    feeds = feedparser.parse(url)

    working_date = dt.datetime.today() - dt.timedelta(7)
    i = 1
    for feed in feeds.entries:
        datetime_object = dt.datetime.strptime(str(feed.published).rstrip(" GMT"), '%a, %d %b %Y %H:%M:%S')
        # published_date = dt.datetime.today().strftime('%a, %d %B %Y %H:%M:%S')
        if datetime_object < working_date:
            break
        i += 1
    return i

def parsing_udm_gov(url):
    i = 0
    udm_news = []
    for k, v in url.items():
        count = feeding_date(v)
        resp = requests.get(v)
        soup_gov = BeautifulSoup(resp.text, 'lxml')
        description_news = []
        for tagD in soup_gov.find_all('description')[:count]:
            content_news = fix_string(tagD.text, k)
            if 100 < len(content_news) and content_news.startswith('Forwarded From') == False:

                if 'Коммерсант' in k and 'бизнес-завтрак' not in content_news \
                        and 'бизнес-пикник' not in content_news \
                        and 'круглый стол' not in content_news:
                    # print(k)
                    i += 1
                    description_news.append(content_news)
                elif 'kommersant' not in content_news and 'Коммерсант' not in k:
                    i += 1
                    description_news.append(content_news)




        for descript in description_news:
            descript = descript.replace('"', '\'').rstrip(']]>')
            article = (descript[:35] + '...') # if len(descript) > 75 else (descript[:25] + '...')
            pos = article.find('http')
            article = article[:pos - 1] + '...'
            article = re.sub(r'http[^(\s)]+', '...', article)
            date = dt.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            content = (article, descript, k, date)
            udm_news.append(content)
    return udm_news

