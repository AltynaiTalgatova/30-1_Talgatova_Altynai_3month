from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, ADMINs
from database.mybot_db import sql_command_all, sql_command_delete


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


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("You are not my boss!")
    else:
        mentors = await sql_command_all()
        for mentor in mentors:
            await message.answer(
                f"{mentor[1]}, {mentor[2]}, {mentor[3]}, {mentor[-1]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"Delete {mentor[1]}",
                                         callback_data=f"delete {mentor[0]}")
                ))


async def complete_delete(callback: types.CallbackQuery):
    await sql_command_delete(callback.data.replace("delete ", ""))
    await callback.answer("Mentor has been removed from database!", show_alert=True)
    await callback.message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda callback: callback.data and callback.data.startswith("delete ")
    )
