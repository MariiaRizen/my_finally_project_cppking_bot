from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


recipe_ikb = InlineKeyboardButton('/Рецепт')
forward_ikb = InlineKeyboardButton('>')
back_ikb = InlineKeyboardButton('<')

ikb_menu = InlineKeyboardMarkup(row_width=2)
ikb_menu.add(recipe_ikb).add(forward_ikb, back_ikb)


