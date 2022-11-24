import logging

from loguru import logger

from loader import bot
from utils.notify_admins import on_startup_notify

from utils.set_bot_commands import set_default_commands
import middlewares
import handlers
import filters
filters.setup_filters(bot)


bot.polling(non_stop=True)


