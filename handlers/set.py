from loader import bot, black_list
import sqlite3
import random

# @bot.message_handler(commands=["set_all"])
# def set_all(message):
#     db=sqlite3.connect('DATA_USER.db')
#     sql=db.cursor()
    
#     i=0
#     while i<10:
#         id1=random.randint(130000, 477777)
#         name=f"test{i}"
#         contact =f"@test{i}"
#         sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (id1, name, contact))
#         db.commit()
#         i+=1
    
#     k=1
#     for l in black_list:
#         name=f"BL{k}"
#         contact =f"@lololol"
#         sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (l, name, contact))
#         db.commit()
        
#     bot.send_message(message.chat.id, "Создано")

