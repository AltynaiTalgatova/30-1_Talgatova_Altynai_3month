# HW 3
# 1 Создайте FSM для создания менторов в отдельном файле fsm_mentor.
# 2 Пример запрашиваемых данных:
# Имя ментора
# Направление
# Возраст ментора
# Группа
# Все это нужно записать в кэш, как на уроке, только для менторов
# Должно работать только для Админа (Куратора) БОТА

from aiogram import executor
import logging
from config import dp
from handlers import commands, callback, extra, admin, fsm_mentor

commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_fsm_mentor(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
