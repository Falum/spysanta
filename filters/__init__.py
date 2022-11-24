from filters.admin_filter import AdminFilter
from filters.lichka import lichka

def setup_filters(bot):
    bot.add_custom_filter(AdminFilter())
    bot.add_custom_filter(lichka())
