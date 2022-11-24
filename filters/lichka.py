from telebot.custom_filters import SimpleCustomFilter

from data.config import ADMINS


class lichka(SimpleCustomFilter):
    

    key = 'lichka'

    def check(self, message):
        if message.chat.type == 'supergroup':
            return True
