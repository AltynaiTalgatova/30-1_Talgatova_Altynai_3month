# 1 Создать своего бота !
# 2 Проделать все настройки (включая скрытие токен ключа бота) !
# 3 Придумайте любую викторину из двух вопросов !
# 4 Написать hendler, который принимает команду мем и отправляет любой мем или прикольную картинку !
# 5 В случае если пустой message hendler принимает число, он должен отправлять ее же, возведенную в квадрат.
# Иначе отправляет то же самое (эхо) !


from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging


TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

print(TOKEN)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f'Good day {message.from_user.full_name}')     # нужно указывать куда chat.id и что отправлять
    # await message.answer('This is an answer method')     # нужно только указывать что отправлять
    # await message.reply('This is a reply method')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton('NEXT', callback_data='next_button_1')
    markup.add(next_button)

    question = "Whose superpower is Fire?"
    answers = [
        "Kim Joonmyun",
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


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
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
    )


@dp.message_handler(commands=['meme'])
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


@dp.message_handler(content_types=['sticker'])
async def echo(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


@dp.message_handler()
async def echo(message: types.Message) -> None:
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text)**2)
    else:
        await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)     # старт бота
