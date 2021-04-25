from datetime import datetime
from parsing_news import parsing_udm_gov
import re

# url = {'Карточный домик. Удмуртия': "https://rsshub.app/telegram/channel/HouseofcardsUdm"}
# news = parsing_udm_gov(url)
#
# print(news)
# print(datetime.now().strftime("%d-%m-%y %H:%M:%S"))

# print(len('Сарапул. Показуха «Единой России» перед выборами, делают вид, что участвуют в уборке.'))
article = "60 случаев заражения коронавирусом выявили в Удмуртии за суткиhttps://www.k... For a fourth day in a row, India has set an unwelcome world record for the number of new coronavirus infections: a further 349,691 cases in the 24 hours to Sunday morning, with another 2,767 lives lostThe capital, Delhi, is one of the worst-hit areas23The BBC's Vikas Pandey reports from a city whose hospitals are overwhelmed and whose citizens are in desperation."
pattern = r'[a-z][A-Z]|\d[A-Z]|[а-я][А-Я]|[а-я][a-z]|\d[a-z]|\d[а-я]|[а-я][A-Z]'
result_find = re.findall(pattern, article)
for match in result_find:
    article = article.replace(match, ' '.join(match))
# print(article)

text = '''Еще 59 случаев заражения коронавирусом выявили в Удмуртии https://www.kommersant.ru/doc/4791199Коммерсантъ
                        Еще 59 случаев заражения коронавирусом выявили в Удмуртии В Удмуртии выявили 59 случаев заражения коронавирусом за минувшие сутки. Кроме того, скончалась одна инфицированная 59-летняя пациентка, сообщает оперштаб региона.Среди заболевших 27 жителей Ижевска, 14 граждан из Сарапула, по три — из Глазова, Дебесского…'''
text2 = '''Полпред президента в ПФО заявил о необходимости увеличить темпы вакцинации от COVID-19 в Удмуртии  https://www.kommersant.ru/doc/4790963Коммерсантъ
                        Полпред президента в ПФО заявил о необходимости увеличить темпы вакцинации от COVID-19 в Удмуртии Полномочный представитель президента РФ в ПФО Игорь Комаров на совещании в Ижевске акцентировал внимание на необходимости увеличения темпов вакцинации. Он отметил, что важную роль в нормализации эпидемиологической обстановки играет массовая вакцинация, сообщает…'''

text3 = '''
Темная Удмуртия:
⚡️Путин объявил все дни с 1 по 10 мая выходными.
«Если вы считаете, что это необходимо, хорошо, мы так и сделаем. Сегодня я соответствующий указ подпишу»: #Путин согласился с предложением Поповой объявить рабочие дни между двумя майскими праздниками выходными.России предстоят 10-дневные майские каникулы.'''

text3 = text3.strip()
if 'https://www.kommersant.ru' in text:
    good_text2 = text2.split('https://www.kommersant.ru')[0]
if text3.startswith('Темная Удмуртия:'):
    text3 = text3.lstrip('Темная Удмуртия:')
print(text3)