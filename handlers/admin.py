from aiogram import types, Dispatcher
from config import bot, ADMINs


async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINs:
            await message.answer('You are not my boss!')
        elif not message.reply_to_message:
            await message.answer('The command must be a response to a message')
        else:
            await message.reply_to_message.pin()
            await message.answer(
                f"{message.from_user.first_name} pinned"
                f"{message.reply_to_message.from_user.full_name}'s message"
            )
    else:
        await message.answer('Write in the group!')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
