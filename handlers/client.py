import os
from aiogram import types, Dispatcher
from aiogram.types import InputFile
from dotenv import load_dotenv
from creat_bot import bot, dp
from boards.keyboards import kb_client, kb_menu
from boards.inley import ikb_menu
from db import db_helpers
from enums.sections import category_mapper


load_dotenv()


HELP_COMMANDS = """
<b>/start</b> - <em>запустити бот</em>
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>опис бота</em>
<b>/Меню</b> - <em>переглянути меню</em>"""
description_text = """Бот з радістю допоможе підібрати смачний рецепт для Вас. Тут є більше 1000 рецептів на будь-який смак 🍱"""


async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await bot.send_sticker(message.chat.id,
                           sticker='CAACAgIAAxkBAAEHkmdj3MN9pdQX3IdtCNblLnOHeCnPkAACGwADwDZPE329ioPLRE1qLgQ',
                           reply_markup=kb_client)
    await bot.send_message(message.chat.id,
                           text=f"Привіт,{message.from_user.first_name}!Я твій бот, який допоможе тобі підібрати хороший рецепт на будь-який смак!",
                           )
    await message.delete()


async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMANDS,
                        parse_mode='HTML')


async def description_command(messege: types.Message):
    await messege.answer(text=description_text)


async def send_menu(message: types.Message):
    await message.answer(text='Виберіть розділ, який Вас цікавить 🍴',
                         reply_markup=kb_menu)


async def sections_handler(message: types.Message):
    category = message.text[1:]
    js = db_helpers.get_first_category_recipy(category)
    await send_recipe_preview(message.chat.id, js)


async def send_recipe_preview(chat_id, js):
    resp_html = js['title']
    img_path = os.path.join(os.environ['DATA_DIR'], js['image_path'])
    cat = InputFile(img_path)
    await bot.send_photo(chat_id=chat_id,
                         photo=cat,
                         caption=resp_html,
                         reply_markup=ikb_menu)


def information_about_recipe(js):
    description = js['description'].split('\nЧитайте також\n')[0].strip()
    recipe = '\n\n'.join([description, js['ingredients'], js['steps']])
    return recipe


async def callback_recipe(callback: types.CallbackQuery):

    js = db_helpers.get_recipy_by_title(callback.message.caption)
    if callback.data == 'Повний опис':
        info_of_recipe = information_about_recipe(js)
        await bot.send_message(chat_id=callback.message.chat.id, text=info_of_recipe, parse_mode='HTML')
    else:
        forward_direction = callback.data == 'вперед'
        js = db_helpers.get_neighbour_recipy(js['id'], js['category'], forward_direction)
        await send_recipe_preview(callback.message.chat.id, js)
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)


categories = list(category_mapper.values())
print(categories)
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(description_command, commands=['description'])
    dp.register_message_handler(send_menu, commands=['Меню'])
    dp.register_message_handler(sections_handler, commands=categories)
    dp.register_callback_query_handler(callback_recipe)
