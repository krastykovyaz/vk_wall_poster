# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
# from sqlite3 import Error

import random

# normalization
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

from difflib import SequenceMatcher  # check similarity


# Preprocess function
def preprocess_text_NLTK(text):
    mystem = Mystem()
    russian_stopwords = stopwords.words("russian")
    tokens = mystem.lemmatize(str(text).lower())
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]
    text = " ".join(tokens)

    return text


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT OR IGNORE INTO news(id, name, description, source, status, createDate) VALUES(?, ?, ?, ?, ?, ?)',
                      entities)
    con.commit()


def sql_length(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM news')
    rows = cursorObj.fetchall()
    return len(rows)


def check_exist(con, descrip):
    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT EXISTS(SELECT 1 FROM news WHERE description="{descrip}")')
    ifex = cursorObj.fetchall()
    if ifex[0][0] < 1 and cursorObj.execute('SELECT * FROM news').rowcount != 0:
        cursorObj.execute('SELECT description FROM news')
        text = cursorObj.fetchall()
        texts = []
        for t in text:
            texts.append(t[0])
        return texts
    return None


def IsTheSame(descrip, db_list_text):
    if db_list_text == False:
        return True
    if db_list_text is None:
        return False
    for store_text in db_list_text:
        norm_store_text = preprocess_text_NLTK(store_text)
        norm_description = preprocess_text_NLTK(descrip)
        if similar(norm_store_text, norm_description) > 0.4:
            return False
    return True


def add2db(con, post):
    article, descript, source, dt = post
    id = (0 if sql_length(con) is None else sql_length(con) + 1)
    if IsTheSame(descript, check_exist(con, descript)):
        entities = (id, article, descript, source, "new", dt)
        sql_insert(con, entities)
