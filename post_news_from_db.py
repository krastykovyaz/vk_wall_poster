import datetime as dt



def post_new(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT id_uniq, name, description, source  FROM news WHERE status = 'new' LIMIT 1")
    rows = cursorObj.fetchall()
    for row in rows:
        return row
    return None


def drop_old(con, today):
    days = dt.timedelta(7)
    del_date = today - days
    del_date = str(del_date.strftime('%d-%m-%y'))
    print(del_date)
    cursorObj = con.cursor()
    cursorObj.execute(f"DELETE FROM news WHERE createDate LIKE '{del_date}%'")
    con.commit()


