from aiogram import executor
import logging
from config import dp, ADMINs, bot
from handlers import commands, callback, extra, admin, fsm_mentor, notifications
from database.mybot_db import sql_create


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_fsm_mentor(dp)
extra.register_handlers_extra(dp)


async def on_startup(dp):
    sql_create()
    await bot.send_message(ADMINs[0], "Hello")
    await notifications.set_scheduler()


async def on_shutdown(dp):
    await bot.send_message(ADMINs[0], "Bye Bye!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
