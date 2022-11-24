from telebot import types

from loader import bot


@bot.message_handler(commands=['echo'])
def start_handler(message: types.Message):
    print(message)