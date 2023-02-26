from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5703001885:AAESJiWPIOk-D6wfdccfFyZPxORIHXTsxd8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())