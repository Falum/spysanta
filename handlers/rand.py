from telebot import types
import sqlite3
import random
from .res_but import button

from loader import bot, black_list



@bot.message_handler(commands=["begin_swap"], chat_types=["supergroup"])
def swap(message):
    bot.delete_message(message.chat.id, message.id)
    
    sqlite_connection = sqlite3.connect('DATA_USER.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    
    spisok = []
    
    for row in records:
        spisok.append(row[0])
    rand = spisok.copy()
    cursor.close()
    random.shuffle(rand)

    white = spisok.copy()
    for m in black_list:
        white.remove(m)
    
    black_to = spisok.copy()
    black_to.remove(456916980)
    black_to.remove(1475230407)
    
    VIP = (456916980,1475230407)
    
    

    prisvoit(spisok, VIP, white, message)   # rand, white, black_to,

def prisvoit(spisok, VIP, white, message):
    
    itog = {}
    full_stuck = spisok.copy()

    for i in VIP:
        prop=check(i, white)

        white.remove(prop)
        full_stuck.remove(prop)
        spisok.remove(i)
        itog[i]=prop


    for_black = full_stuck.copy()
    
    for_black.remove(456916980)
    for_black.remove(1475230407)


    for k in black_list:
        ira = check(k, for_black)

        full_stuck.remove(ira)
        for_black.remove(ira)
        spisok.remove(k)
        itog[k]=ira

    for u in spisok:
        lol = check(u, full_stuck)

        full_stuck.remove(lol)
        itog[u]=lol

    
    to_table(itog, message)




def check(kto, spis):
    while True:
        komu=random.choice(spis)
        if kto == komu:
            pass
        else:
            break
    return(komu)




def to_table(itog, message):
    
    for i in itog:


        db=sqlite3.connect('DATA_USER.db')
        sql=db.cursor()
                        
        sql.execute(f"INSERT INTO random VALUES(?, ?)", (i, itog[i]))
        db.commit()


    button(message)