from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp




# @dp.callback_query_handler(text="button_call_1")
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


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)

    question = "Какая помада является прозрачной и используется скорее для ухода за губами, нежели для красоты?"
    answers = [
        "Питательная",
        "Увлажняющая",
        "Гигиеническая",

    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Думай",
        open_period=15,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    question = "Что такое консилер?"
    answers = [
        "Подводка для глаз",
        "Средство для губ",
        "Маскирующее средство",

    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Серьёзно не знаешь?!",
    )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4,
                                        lambda call: call.data == "button_call_3")