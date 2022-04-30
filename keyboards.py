from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

button1 = KeyboardButton('Меню 🍝')
button2 = KeyboardButton('Вільні столики 🪑')

golovna = ReplyKeyboardMarkup().row(
    button1, button2
).add(KeyboardButton('Замовити столик!🛎'))

button4 = KeyboardButton('Мої резервації 🗝')
button5 = KeyboardButton('Про бота ⚙️')
golovna.row(button4, button5)

#Меню ресторану
snidanokm = KeyboardButton('Сніданок')
lunchm = KeyboardButton('Обід')
drinksm = KeyboardButton('Напої')
nazad = KeyboardButton('До головного меню')

markmenu = ReplyKeyboardMarkup().add(
    snidanokm).add(lunchm).add(drinksm).add(
    nazad)

#Сніданок меню
snidanokit = KeyboardButton('Сніданок Італійський')
snidanokuk = KeyboardButton('Сніданок Англійський')
snidanokf = KeyboardButton('Сніданок Французький')
nazaddomenu = KeyboardButton('Назад до меню')
marksnidanok = ReplyKeyboardMarkup().add(
    snidanokit).add(snidanokuk).add(snidanokf).add(
    nazaddomenu)


# drinksmenu
drink1 = KeyboardButton('Вода')
drink2 = KeyboardButton('Сік')
drink3 = KeyboardButton('Чай')
drink4 = KeyboardButton('Кава')
markdrink = ReplyKeyboardMarkup().add(
    drink1).add(drink2).add(drink3).add(drink4).add(
    nazaddomenu)

#Обід меню
obidit = KeyboardButton('Обід Італійський')
obiduk = KeyboardButton('Обід Англійський')
obidf = KeyboardButton('Обід французький')
markobid = ReplyKeyboardMarkup().add(
    obidit).add(obiduk).add(obidf).add(
    nazaddomenu)

#Back
glmn = ReplyKeyboardMarkup().add(
    nazad)

#Резервація столу
stil1 = KeyboardButton('Столик 1')
stil2 = KeyboardButton('Столик 2')
stil3 = KeyboardButton('Столик 3')
stil4 = KeyboardButton('Столик 4')
stil5 = KeyboardButton('Столик 5')
markstil = ReplyKeyboardMarkup().add(
    stil1).add(stil2).add(stil3).add(stil4).add(stil5).add(
    nazad)


delres = KeyboardButton('Видалити мої резервації')
resdel = ReplyKeyboardMarkup().add(delres).add(
    nazad)