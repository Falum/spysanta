from telebot import types
import sqlite3
from filters.lichka import lichka
from loader import bot


@bot.message_handler(commands=['start'], chat_types=["supergroup"])
def start_handler(message: types.Message):
    bot.send_message(message.chat.id,
                     f"Hello, {message.from_user.full_name}, {message.chat.type}!")
    
    db=sqlite3.connect('DATA_USER.db')    
    sql=db.cursor()
    
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
        Id INT,
        Account_Name TEXT,
        Contact TEXT
    )""")

    sql.execute("""CREATE TABLE IF NOT EXISTS random(
        ID_from INT,
        ID_in INT
    )""")
    db.commit()
