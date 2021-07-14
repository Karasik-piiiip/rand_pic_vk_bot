import sqlite3

def table(user_id = None, chat_id = None):
	"""Добавляем пользователя или чат в БД, если их там нет """
    cur = con.cursor()
    cur.execute('create table if not exists Users (id INTEGER UNIQUE)')
    cur.execute('create table if not exists Chats (id INTEGER UNIQUE)')
    if user_id != None:
        cur.execute('insert or ignore into Users values(?)', (user_id,))
        con.commit()
    if chat_id != None:
        cur.execute('insert or ignore into Chats values(?)', (chat_id,))
        con.commit()
    cur.close()

def get_table():
    cur = con.cursor()
    users = [users[0] for users in cur.execute("SELECT id FROM Users")]
    chats = [chats[0] for chats in cur.execute("SELECT id FROM Chats")]
    cur.close()
    return users, chats
