#!/usr/bin/python

import vk_api
import requests, time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# community_token = "token"
community_token = 'token'
params = (
    ('group_ids', 'peredamsu'),
    ('access_token', community_token),
    ('v', '5.130')
)

# response = requests.get('https://api.vk.com/method/groups.getById', params=params)

# print(response.text)


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# url = "https://newssearch.yandex.ru/yandsearch?text=граховский&rpt=nnews2&grhow=clutop&rel=rel&within=8"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, "html.parser")
# print(soup.encode("utf-8"))
# table = soup.find_all('table')[1]

driver = webdriver.Chrome(executable_path='./chromedriver')
wait = WebDriverWait(driver, 10)
driver.get('https://newssearch.yandex.ru/news/search?text=%D0%B3%D1%80%D0%B0%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9+%D1%80%D0%B0%D0%B9%D0%BE%D0%BD+date%3A20210419&filter_date=1618855037000')

news_elements = driver.find_elements_by_class_name('news-search-story') 
for item in news_elements:
    # while True:
    # try:
    #     time.sleep(1)
    #     show_more = wait.until(EC.element_to_be_clickable((By.ID, 'u-1618856912000-0a7121-12')))  
    #     show_more.click()
    # except Exception as e:
    #         print("e")
    #         break
    # show_more = wait.until(EC.element_to_be_clickable((By.ID, item)))  
    # show_more.click()
    new = item.text.split('Посмотреть ещё')
    print(new[0])
# print(news_elements.text)

# user_token = 'token'

# params_2 = (
#     ('owner_id', '-193482637'),
#     ('from_group', '1'),  
#     ('message', new[0]),   
#     ('access_token', user_token),
#     ('v', '5.130')     
# )

# response = requests.get('https://api.vk.com/method/wall.post', params=params_2)

# print(response.text)

print ("Headless Firefox Initialized")
driver.quit()