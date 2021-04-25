from parsing_news import parsing_udm_gov
from add_news2db import add2db
from post_news_from_db import post_new, drop_old
from updating_news_db import news_update
from wall_vk_posting import  wall_poster



def job_download(vk_bd, url):
    posts = parsing_udm_gov(url)
    for post in posts:
        add2db(vk_bd, post)


def job_post(vk_bd):
    db_row = post_new(vk_bd)
    if db_row is not None:
        wall_poster(db_row)


def job_update(vk_bd):
    news_update(vk_bd)

def job_delete(vk_bd, today):
    drop_old(vk_bd, today)