from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = 'onfh'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())