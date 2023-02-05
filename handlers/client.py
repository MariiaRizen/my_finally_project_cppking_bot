from aiogram import types, Dispatcher
from creat_bot import bot
from boards.keyboards import kb_client, kb_menu
from db import scripts
import read_json

HELP_COMMANDS = """"
<b>/start</b> - <em>запустити бот</em>
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>опис бота</em>
<b>/Меню</b> - <em>переглянути меню</em>"""

#@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEHkmdj3MN9pdQX3IdtCNblLnOHeCnPkAACGwADwDZPE329ioPLRE1qLgQ', reply_markup=kb_client)
    await bot.send_message(message.chat.id, text=f"Привіт,{message.from_user.first_name}!Я твій бот, який допоможе тобі підібрати хороший рецепт на будь-який смак!",
                           )
    await message.delete()


async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMANDS,
                        parse_mode='HTML')


async def description_command(messege: types.Message):
    await messege.answer(text='Наш бот допоможе з рецептом')
    
#@dp.message_handler(commands=['Меню'])
async def send_menu(message: types.Message):
    # for ret in scripts.cur.execute('Select image, name FROM cooking').fetchall():
    #     await bot.send_photo(ret[0])
    await message.answer(text='Виберіть розділ, який Вас цікавить 🍴',
                         reply_markup=kb_menu)

# async def send_snidanki(message: types.Message):
#     recipe = read_json.read_recipes_file()
#     inform = recipe[0]['category']
#     if inform == 'snidanki':
#         for rec in inform:
#
#             await message.answer(text=rec['image_path'])
#             await message.answer(text=rec['title'])
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(description_command, commands=['description'])
    dp.register_message_handler(send_menu, commands=['Меню'])
    # dp.register_message_handler(send_snidanki, commands=['Сніданки'])
