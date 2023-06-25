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


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel_button = KeyboardButton("Cancel")
cancel_markup.add(cancel_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Yes"),
    KeyboardButton("Re-fill in"),
    cancel_button
)

course_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Backend"),
    KeyboardButton("Frontend"),
    KeyboardButton("UX/UI"),
    KeyboardButton("Android"),
    KeyboardButton("Ios"),
    cancel_button
)
