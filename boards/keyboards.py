from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


help_bt = KeyboardButton('/help')
description_bt = KeyboardButton('/description')
menu_bt = KeyboardButton('/Меню')
soup_bt = KeyboardButton('/Супи')
baking_bt = KeyboardButton('/Випічка')
salad_kb = KeyboardButton('/Салати')
pasta_kb = KeyboardButton('/Паста')
snidanki_kb = KeyboardButton('/Сніданки')
zakuski_kb = KeyboardButton('/Закуски')
drugi_stravu_kb = KeyboardButton('/Другі страви')
maso_kb = KeyboardButton('/Мясо')
ryba_kb = KeyboardButton('/Риба')
ovoce_kb = KeyboardButton('/Овочі')
garnir_kb = KeyboardButton('/Гарнір')
napoi_kb = KeyboardButton('/Напої')
dlya_ditej_kb = KeyboardButton('/Для дітей')
stravi_u_mult_kb = KeyboardButton('/У мультиварці')
varennya_kb = KeyboardButton('/Варення')
desert_kb = KeyboardButton('/Десерт')
pisni_kb = KeyboardButton('/Пісні')
diyetichni_kb = KeyboardButton('/Дієтичні')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(help_bt, description_bt).add(menu_bt)

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(soup_bt, baking_bt, salad_kb, pasta_kb, snidanki_kb, zakuski_kb, drugi_stravu_kb, maso_kb,
            ryba_kb, ovoce_kb, stravi_u_mult_kb, pisni_kb, napoi_kb,
            varennya_kb, desert_kb)



"""insert()добавляє в рядок, якщо є місце
row() всі кнопки в одному рядку"""
