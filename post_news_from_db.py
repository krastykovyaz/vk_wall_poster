import datetime as dt
import sqlite3


def post_new(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT id, name, description, source  FROM news WHERE status = 'new' LIMIT 1")
    rows = cursorObj.fetchall()
    for row in rows:
        return row
    return None


def drop_old(con, today):
    days = dt.timedelta(1)
    del_date = today - days
    del_date = str(del_date.strftime('%d-%m-%Y'))
    cursorObj = con.cursor()
    cursorObj.execute(f"DELETE FROM news WHERE createDate LIKE '%{del_date}%'")
    cursorObj.fetchall()


# con = sqlite3.connect('news_for_vk_db')
# drop_old(con, dt.date(2021, 4, 26))
