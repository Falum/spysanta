from telebot import types
import sqlite3

from loader import bot


@bot.message_handler(commands=['list'], chat_types=["supergroup"])
def start_handler(message):
    sqlite_connection = sqlite3.connect('DATA_USER.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    text = ""
    
    for row in records:
        text+=f"{row[1]}    {row[2]}\n"

    cursor.close()
    
    bot.send_message(message.chat.id,
                     f"Список участников:\n\n"+text)