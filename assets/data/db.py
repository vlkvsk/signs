import sqlite3, datetime, pytz, aiosqlite
from assets.config.cfg import PATH_DATABASE
from datetime import datetime

now = datetime.now()
conn=sqlite3.connect(PATH_DATABASE)
cursor = conn.cursor()

def add_user(user_id, user_name):
    data = cursor.execute(f'SELECT user_id FROM users WHERE user_id = ?', (user_id,)).fetchone()
    timezone = pytz.timezone('Europe/Moscow')
    time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M')
    if data is None:
        sql = "INSERT INTO users (user_id, user_name, balance, banned, reg_time) VALUES (?, ?, ?, ?, ?)"
        val = (user_id, user_name, 0, 0, time)
        cursor.execute(sql, val)
        conn.commit()
        return False
    else:
        pass
        return True

def get_user(user_id):
    data = cursor.execute(f'SELECT user_id FROM users WHERE user_id = ?', (user_id,)).fetchone()
    return True if data else False

def check_ban(user_id):
    c = cursor.execute('SELECT banned FROM users WHERE user_id = ?', (user_id,)).fetchone()
    return c[0] if c else None

async def create_tables_if_not_exist():
    async with aiosqlite.connect(PATH_DATABASE) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, user_name TEXT, balance INTEGER,
                             performer INTEGER, banned INTEGER, deals INTEGER, rating INTEGER, reg_time TEXT)''')
        await db.commit()