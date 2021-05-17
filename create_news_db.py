import sqlite3
from datetime import datetime
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('tmp_news_for_vk_auto2.db')
        return con
    except:
        print("Already exist")

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE news(id INTEGER PRIMARY KEY AUTOINCREMENT, id_uniq integer, name text, description text, source text, status text, createDate text)")
    con.commit()

con = sql_connection()
sql_table(con)

con.close()
