from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


help_bt = KeyboardButton('/help')
description_bt = KeyboardButton('/description')
menu_bt = KeyboardButton('/Меню')
soup_bt = KeyboardButton('/Суп')
baking_bt = KeyboardButton('/Випічка')
salad_kb = KeyboardButton('/Салат')
pasta_kb = KeyboardButton('/Паста')
snidanki_kb = KeyboardButton('/Сніданки')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(help_bt, description_bt).add(menu_bt)

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(soup_bt, baking_bt, salad_kb, pasta_kb, snidanki_kb)



"""insert()добавляє в рядок, якщо є місце
row() всі кнопки в одному рядку"""
