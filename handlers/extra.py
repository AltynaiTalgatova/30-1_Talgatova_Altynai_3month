from aiogram import types, Dispatcher
from config import bot, dp


async def echo_sticker(message: types.Message) -> None:
    # print(message)
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


async def echo_text(message: types.Message) -> None:
    if message.text.lower().startswith('game'):
        await message.answer_dice(emoji='🎯')

    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text)**2)
    else:
        await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_sticker, content_types=['sticker'])
    dp.register_message_handler(echo_text)
