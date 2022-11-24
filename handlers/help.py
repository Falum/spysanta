from telebot import types

from loader import bot


@bot.message_handler(commands=['help'], chat_types=["supergroup"])
def start_handler(message: types.Message):
    bot.send_message(message.chat.id,
                     f"Commands: \n\n"
                     f"/start - Старт??\n"
                     f"/help - Список команд\n"
                     f"/list - Список участников\n"
                     f"/who - Узнать кто выпал")
