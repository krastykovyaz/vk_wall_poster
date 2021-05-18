def looking_news(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT id_uniq, name, description, source  FROM news WHERE status = 'new'")
    rows = cursorObj.fetchall()
    if len(rows) > 0:
        for row in rows:
            return row
    else:
        return None

def sql_update(con, id):
    cursorObj = con.cursor()
    cursorObj.execute(f"UPDATE news SET status = 'posted' where id_uniq = {id}")
    con.commit()

def news_update(con):
    if looking_news(con) is not None:
        id = looking_news(con)[0]
        news_name = looking_news(con)[1]
        news_description = looking_news(con)[2]
        source = looking_news(con)[3]
        sql_update(con, id)
        # news = sql_update(con)
        # print(id)

