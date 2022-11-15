from aiogram import Bot, Dispatcher
from aiogram.utils import executor
import logging
import config
from handlers import callback, client, extra
from config import dp, bot


callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)


# @dp.message_handler(commands=['mem'])
# async def mem1(message: types.Message):
#     photo = open('media/mem.jpg', 'rb')
#     photo = open('media/mem1.jpg', 'rb')
#     photo = open('media/mem2.jpg', 'rb')
#     photo = open('media/mem3.jpg', 'rb')
#     await bot.send_photo(message.from_user.id, photo=photo)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

