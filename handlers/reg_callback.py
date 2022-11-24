from telebot import types
import sqlite3

from loader import bot


@bot.callback_query_handler(func = lambda call: call.data == "registration")
def reg1(call):
    
    db=sqlite3.connect('DATA_USER.db')    
    sql=db.cursor()
    id = call.from_user.id
    
    list = [x[0] for x in sql.execute("select Id from users").fetchall()] # массив с id записей
    if id in list:
        bot.answer_callback_query(callback_query_id=call.id, text="Ты уже записан", show_alert=False)
        # bot.answer_callback_query(callback_query_id=id, text="Изменять голос запрещено", show_alert=False)
    else:
        reg2(call)




def reg2(call):
    db=sqlite3.connect('DATA_USER.db')
    sql=db.cursor()
    
    id = call.from_user.id
    username = call.from_user.first_name
    contact = f"@{call.from_user.username}"

    sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (id, username, contact))
    db.commit()




@bot.callback_query_handler(func = lambda call: call.data == "result")
def info(call):

    db=sqlite3.connect('DATA_USER.db')
    sql=db.cursor()

    sql.execute(f"""SELECT * FROM random WHERE ID_from = {call.from_user.id}""")
    record = sql.fetchall()
    for i in record:
        name = i[1]
        
        sql.execute(f"""SELECT * FROM users WHERE Id = {name}""")
        record2 = sql.fetchall()
        for j in record2:
            account=str(j[1])+f" - "+str(j[2])
        
            bot.answer_callback_query(callback_query_id=call.id, text=account, show_alert=False)

