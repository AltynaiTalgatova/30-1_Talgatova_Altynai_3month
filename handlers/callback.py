from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import dp


# @dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_2')
    markup.add(next_button)

    question = "EXO's first full-length album was?"
    answers = [
        "Obsession",
        "XOXO",
        "The War",
        "Exact",
        "Don't mess up my tempo",
        "Exodus"
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="A fan should know that!",
        open_period=12,
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_3')
    markup.add(next_button)

    question = "Who is the youngest member (maknae) of the group?"
    answers = [
        "Kim Minseok",
        "Kim Jongdae",
        "Byun Baekhyun",
        "Oh Sehun",
        "Zhang Yixing",
        "Park Chanyeol"
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="A fan should know that!",
        open_period=12,
        reply_markup=markup
    )


async def quiz_4(callback: types.CallbackQuery):
    await callback.message.answer("That's all!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='next_button_1')
    dp.register_callback_query_handler(quiz_3, text='next_button_2')
    dp.register_callback_query_handler(quiz_4, text='next_button_3')

