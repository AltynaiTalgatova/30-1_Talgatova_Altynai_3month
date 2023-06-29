from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from . import keyboards
from config import ADMINs
from database.mybot_db import sql_command_insert

class FSMMentor(StatesGroup):
    name = State()
    course = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMINs:
            await message.answer("You're not my boss!")
        else:
            await FSMMentor.name.set()
            await message.answer("What is mentor's name?", reply_markup=keyboards.cancel_markup)
    else:
        await message.reply("Write in private!")


async def load_name(message: types.Message, state: FSMContext):
    if not message.text.lower().isalpha():
        await message.answer('Write in letters!')
    else:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMMentor.next()
        await message.answer("Which course?", reply_markup=keyboards.course_markup)


async def load_course(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['backend', 'frontend', 'ux/ui', 'android', 'ios']:
        await message.answer("Use buttons!")
    else:
        async with state.proxy() as data:
            data['course'] = message.text
        await FSMMentor.next()
        await message.answer("How old is mentor?", reply_markup=keyboards.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Write in numbers!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMMentor.next()
        await message.answer("What group number?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"{data['name']}, {data['course']}, {data['age']}, "
                             f"{data['group']}")
    await FSMMentor.next()
    await message.answer("Is everything correct?", reply_markup=keyboards.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await sql_command_insert(state)
        await state.finish()
        await message.answer("All is ready")
    elif message.text.lower() == 're-fill in':
        await FSMMentor.name.set()
        await message.answer("What is mentor's name?")
    else:
        await message.answer("Use buttons!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Alright!")
    else:
        await message.answer("You haven't started yet.")


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMMentor.name)
    dp.register_message_handler(load_course, state=FSMMentor.course)
    dp.register_message_handler(load_age, state=FSMMentor.age)
    dp.register_message_handler(load_group, state=FSMMentor.group)
    dp.register_message_handler(submit, state=FSMMentor.submit)
