from telebot import types
from keyboards.call_back import reg
from loader import bot


@bot.message_handler(commands=['start_dvizh'], chat_types=["supergroup"])
def start_handler(message: types.Message):
    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id,
                     f"Нажми для участия в Тайном Санте", reply_markup=reg)