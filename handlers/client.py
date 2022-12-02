from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
# from keyboards.client_kb import start_markup
from parser import dina_bags


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здравствуй {message.from_user.first_name}")
    await message.answer("This is an answer method!")
    await message.reply("This is an reply method!")


async def mem1(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    photo = open('media/mem1.jpg', 'rb')
    photo = open('media/mem2.jpg', 'rb')
    photo = open('media/mem3.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Если вам грустно, добавьте на губы немного помады и…"
    answers = [
        'Улыбнитесь',
        'Закажите шампанского',
        'Накрасьте ресницы тушью',
        'Атакуйте',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="От...станет всем теплей )",
        open_period=10,
        reply_markup=markup
    )


async def gg(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply('Надо ответить сообщением')


async def parser_bags(message: types.Message):
    data = dina_bags.parser()
    for item in data:
        await bot.send_message(message.from_user.id, f"{item['brand']}\n\n"
                                                     f"{item['link']}\n\n"
                                                     f"{item['price']}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem1, commands=['mem'])
    dp.register_message_handler(gg, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(parser_bags, commands=['bags'])
x