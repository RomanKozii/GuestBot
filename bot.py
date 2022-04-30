from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import TOKEN
import keyboards as kb
import config as mn
import sqlite3


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#__________________________________________
@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,'Доброго дня!\nЯ бот ресторану Roma.\nЗагялньте в меню щоб дізнзнатисьатись про мої функції', reply_markup=kb.golovna)
    await bot.send_sticker(msg.chat.id, "CAACAgIAAxkBAAEEl5hibF5my-pCI-9yFh216zSvb5hm1AACNQADg_ioGnGqTswaDQTeJAQ")
    try:
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO users VALUES("{msg.from_user.id}", "@{msg.from_user.username}")')
        conn.commit()
    except Exception as e:
        print(e)
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO users VALUES("{msg.from_user.id}")')
        conn.commit()


#___________________________________________
@dp.message_handler(text="Меню 🍝")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Вибирайте що бажаєте:", reply_markup=kb.markmenu)

@dp.message_handler(text="Сніданок")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Ось що ви можете скуштувати на сніданок:", reply_markup=kb.marksnidanok)
@dp.message_handler(text="Сніданок Італійський")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, mn.sit , reply_markup=kb.marksnidanok)

@dp.message_handler(text="Сніданок Англійський")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, mn.suk , reply_markup=kb.marksnidanok)

@dp.message_handler(text="Сніданок Французький")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, mn.sf , reply_markup=kb.marksnidanok)
@dp.message_handler(text="Обід")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Ось що ви можете скуштувати на обід:", reply_markup=kb.markobid)

@dp.message_handler(text="Обід Італійський")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, mn.oit , reply_markup=kb.markobid)

@dp.message_handler(text="Обід Англійський")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, mn.ouk , reply_markup=kb.markobid)

@dp.message_handler(text="Обід французький")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, mn.of , reply_markup=kb.markobid)

@dp.message_handler(text="Напої")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Меню наших напоїв:", reply_markup=kb.markdrink)
#_____________________________________________

@dp.message_handler(text="Вільні столики 🪑")
async def memu_rest(msg: types.Message):
    conn = sqlite3.connect('menu.db')
    cur = conn.cursor()
    cur.execute(f'SELECT nomber FROM tables WHERE Employment = "free"')
    result = cur.fetchall()
    print(result)
    await bot.send_message(msg.from_user.id, f'Вільні столики:\n{(result)}', reply_markup=kb.glmn)
#_______________________________________________


#_______________________________________________
@dp.message_handler(text="Замовити столик!🛎")
async def stol_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id,"Оберіть Столик:", reply_markup=kb.markstil)

#_______Cтіл_1___________
@dp.message_handler(text="Столик 1")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db') #INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'UPDATE tables  SET reservation = "{msg.from_user.id}" WHERE nomber = "1"')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Столик номер 1:\nЗарезервовано!", reply_markup=kb.markstil)
    except Exception as e:
        print(e)
        conn = sqlite3.connect('menu.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO tables (reservation) VALUES("{msg.from_user.id}")')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)


#___________________________
@dp.message_handler(text="Столик 2")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db') #INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'UPDATE tables  SET reservation = "{msg.from_user.id}" WHERE nomber = "2"')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Столик номер 2:\nЗарезервовано!", reply_markup=kb.markstil)
    except Exception as e:
        print(e)
        conn = sqlite3.connect('menu.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO tables (reservation) VALUES("{msg.from_user.id}")')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)

@dp.message_handler(text="Столик 3")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db') #INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'UPDATE tables  SET reservation = "{msg.from_user.id}" WHERE nomber = "3"')
        conn.commit()
        await bot.send_message(msg.from_user.id, "ССтолик номе 3:\nЗарезервовано!", reply_markup=kb.markstil)
    except Exception as e:
        print(e)
        conn = sqlite3.connect('menu.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO tables (reservation) VALUES("{msg.from_user.id}")')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)

@dp.message_handler(text="Столик 4")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db')  # INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'UPDATE tables  SET reservation = "{msg.from_user.id}" WHERE nomber = "4"')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Столик номе 4:\nЗарезервовано!", reply_markup=kb.markstil)
    except Exception as e:
        print(e)
        conn = sqlite3.connect('menu.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO tables (reservation) VALUES("{msg.from_user.id}")')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)

@dp.message_handler(text="Столик 5")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db') #INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'UPDATE tables  SET reservation = "{msg.from_user.id}" WHERE nomber = "5"')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Столик номе 5:\nЗарезервовано!", reply_markup=kb.markstil)
    except Exception as e:
        print(e)
        conn = sqlite3.connect('menu.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO tables (reservation) VALUES("{msg.from_user.id}")')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)



#____________________________________________
@dp.message_handler(text="Мої резервації 🗝")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db')  # INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'SELECT name FROM tables WHERE reservation = "{msg.from_user.id}" ')
        resultres = cur.fetchall()
        print(resultres)
        await bot.send_message(msg.from_user.id, f'Ваш столик під номером:\n{(resultres)}', reply_markup=kb.resdel)
    except Exception as e:
        print(e)
        conn = sqlite3.connect('menu.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO tables (reservation) VALUES("{msg.from_user.id}")')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)
#________________________


@dp.message_handler(text="Видалити мої резервації")
async def memu_rest(msg: types.Message):
    try:
        conn = sqlite3.connect('menu.db')  # INSERT INTO tables(reservation)
        cur = conn.cursor()
        cur.execute(f'UPDATE tables  SET reservation = null WHERE reservation = "{msg.from_user.id}"')
        conn.commit()
        await bot.send_message(msg.from_user.id, "Резервація відмінена!", reply_markup=kb.glmn)
    except Exception as e:
        print(e)
        await bot.send_message(msg.from_user.id, "Якась помилка!\nПопробуйте ще раз", reply_markup=kb.glmn)

#_________________________________________________
@dp.message_handler(text="До головного меню")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id,"Ви повернулись до головного меню", reply_markup=kb.golovna)

@dp.message_handler(text="Назад до меню")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id,"Ви повернулись до меню", reply_markup=kb.markmenu)

#___________________________________________
@dp.message_handler(text="Про бота ⚙️")
async def memu_rest(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Меню ресторану бот:\nСвторений для проєкту курсової роботи\nСтудента: Козія Романа", reply_markup=kb.golovna)

if __name__ == '__main__':
    executor.start_polling(dp)