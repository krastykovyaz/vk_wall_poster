import random, sqlite3
from datetime import datetime
from time import sleep
from poster_constructor import job_download, job_post, job_update, job_delete
vk_bd = sqlite3.connect('tmp_news_for_vk_auto2.db')

FREQ_PER_HOUR = 2
SECONDS_IN_HOUR = 3

DURATION = int(SECONDS_IN_HOUR / FREQ_PER_HOUR)
DELTA_MIN = int(DURATION / 2)
SECOND_SLEEP = 0

START_HOUR = 3600
STOP_HOUR = 18
every_three = 0

url = {
    'Стопкоронавирус.Удмуртия': 'https://rsshub.app/telegram/channel/covid19udm',
    'Правительство Удмуртии': "https://rsshub.app/telegram/channel/udmurt_gov",
    'Коммерсантъ - Удмуртия': "https://rsshub.app/telegram/channel/kommersant18",
    'Темная Удмуртия': "https://rsshub.app/telegram/channel/black_udm",
    'Карточный домик. Удмуртия': "https://rsshub.app/telegram/channel/HouseofcardsUdm",
    'life18': "https://rsshub.app/telegram/channel/life_udmurtia"
}

while True:
    saved_time = datetime.now()
    sleep_seconds = random.randint(max(SECOND_SLEEP, DELTA_MIN), SECOND_SLEEP + DURATION)
    sleep(sleep_seconds)
    time_now = datetime.now()
    if START_HOUR < time_now.hour <= STOP_HOUR:
        print('Posting...')
        job_post(vk_bd)
        job_update(vk_bd)
        every_three += 1
    if every_three % 3 == 0:
        print('Downloading...')
        job_download(vk_bd, url)
    if 1 < time_now.hour < 2:
        print('Deleting...')
        job_delete(vk_bd, time_now.date())
    SECOND_SLEEP = DURATION - sleep_seconds
    print((datetime.now() - saved_time).seconds)

vk_bd.close()

