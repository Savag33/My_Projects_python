import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor() #Cursor
    # так автоматом закрываеться подкючение

    #удаление
    cur.execute("DROP TABLE IF EXISTS users")

    # создание таблицы                         # ограничения
    cur.execute("""CREATE TABLE IF NOT EXISTS users 
    (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    sex INTEGER DEFAULT 1,
    old INTEGER NOT NULL DEFAULT 1,
    score INTEGER) """)

    # AUTOINCREMENT каждый раз увеличивает id на +1

