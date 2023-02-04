from aiogram.utils import executor
from creat_bot import dp
from handlers import client, other

async def on_startup(_):
    print('Бот почав працювати')


client.register_handlers_client(dp)
other.register_handlers_other(dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

