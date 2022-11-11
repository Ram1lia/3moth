from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config
import logging
import random

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здравствуй {message.from_user.first_name}")
    await message.answer("This is an answer method!")
    await message.reply("This is an reply method!")

@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Из чего изготавливают кармин, натуральный пищевой краситель, используемый в косметике?"
    answers = [
        "Из растений",
        "Из минералов",
        "Из наскомых",

    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="энтомофо́бия - это боязнь..",
        open_period=15,
        reply_markup=markup
    )

@dp.message_handler(commands=['mem'])
async def mem1(message: types.Message):
    photo = open("media", 'rb')
    photo = random.choice()
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

