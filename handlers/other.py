from aiogram import types, Dispatcher
from creat_bot import dp, bot



#@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo)
