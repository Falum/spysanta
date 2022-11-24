from telebot import types
from keyboards.call_back import info
from loader import bot



@bot.message_handler(commands=['who'], chat_types=["supergroup"])
def button(message: types.Message):

    bot.send_message(message.chat.id,
                     f"<b>Что бы узнать кто тебе выпал, нажми кнопку ниже</b>\n\n<i>Имя этого человека будет в всплывающем уведомлении</i>", reply_markup=info)
