from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from .keyboards import start_markup
from aiogram.dispatcher.filters import Text
from database.mybot_db import sql_command_random


async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f'Good day {message.from_user.full_name}',
                           reply_markup=start_markup)


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_1')
    markup.add(next_button)

    question = "Whose superpower is Fire?"
    answers = [
        "Kim Junmyeon",
        "Byun Baekhyun",
        "Park Chanyeol",
        "Do Kyungsoo",
        "Kim Jongin",
        "Oh Sehun",
    ]

    await message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="A fan should know that",
        open_period=12,
        reply_markup=markup
    )


async def meme_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo='https://i.pinimg.com/564x/70/a7/99/70a7992bfb93ea8db8fe34be15387374.jpg',
        caption='Когда пытаешься понять как отправить фото в телеграм боте'
    )

    photo = open('media/Sehun.jpeg', 'rb')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption='Когда код заработал с первого раза'
    )


async def get_random_mentor(message: types.Message) -> None:
    random_mentor = await sql_command_random()
    await message.answer(f"{random_mentor[1]}, {random_mentor[2]}, {random_mentor[3]}, "
                         f"{random_mentor[-1]}")


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(get_random_mentor, Text(equals="get", ignore_case=True))
