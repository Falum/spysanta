from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Token
ADMINS = list(map(int, env.list("ADMINS")))  # Admins
BLACK_LIST = list(map(int, env.list("BLACK_LIST")))
