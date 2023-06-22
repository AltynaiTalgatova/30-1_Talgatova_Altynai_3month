from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton('/start')
quiz_button = KeyboardButton('/quiz')
meme_button = KeyboardButton('/meme')

start_markup.add(
    start_button,
    quiz_button,
    meme_button
)