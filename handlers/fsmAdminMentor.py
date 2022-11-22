from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboads.client_kb import submit_markup, cancel_markup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.bot_db import sql_command_insert, sql_command_delete, sql_command_random, sql_command_all, sql_create, \
    sql_commands_get_all_id


class FSMMentor(StatesGroup):
    name = State()
    age = State()
    direction = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMMentor.name.set()
        await message.answer("Здравствуй, как зовут?",
                             reply_markup=cancel_markup)
    else:
        await message.answer("Пиши в личку!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMMentor.next()
    await message.answer("Сколько лет?")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 17 < int(message.text) < 50:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMMentor.next()
            await message.answer('Какое направление?', reply_markup=submit_markup)

    except:
        await message.answer('Такого направления нет.')


async def direction(message: types.Message, state: FSMContext):
    async  with state.proxy() as data:
        data['direction'] = message.text
    await FSMMentor.next()
    await message.answer('Какая группа?')


async def load_group(message: types.Message, state: FSMContext):
    async  with state.proxy() as data:
        data['group'] = int(message.text)
        await bot.send_message(message.chat.id,
                               f"Имя: {data['name']} \n"
                               f" Возраст: {data['age']}\n  "
                               f"Направление: {data['direction']}\n"
                               f"Группа: {data['group']}")
    await FSMMentor().next()
    await message.answer('Все верно?')


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await message.answer("kmngjbjdfvndkfjgndjrgk")
        await state.finish()
        await message.answer(')')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отмена')
    else:
        await message.answer('...')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отмена')


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMMentor.name)
    dp.register_message_handler(load_age, state=FSMMentor.age)
    dp.register_message_handler(direction, state=FSMMentor.direction)
    dp.register_message_handler(load_group, state=FSMMentor.group)
    dp.register_message_handler(submit, state=FSMMentor.submit)
