from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


recipe_ikb = InlineKeyboardButton('Рецепт', callback_data='повний опис')
forward_ikb = InlineKeyboardButton('<', callback_data='вперед')
back_ikb = InlineKeyboardButton('>', callback_data='назад')

ikb_menu = InlineKeyboardMarkup(row_width=2)
ikb_menu.add(recipe_ikb).add(forward_ikb, back_ikb)


