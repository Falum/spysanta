from telebot import types


reg = types.InlineKeyboardMarkup()
but1 = types.InlineKeyboardButton(text = "Принять участие", callback_data="registration")
reg.add(but1)


info = types.InlineKeyboardMarkup()
but2 = types.InlineKeyboardButton(text = "Узнать кому дарю", callback_data="result")
info.add(but2)