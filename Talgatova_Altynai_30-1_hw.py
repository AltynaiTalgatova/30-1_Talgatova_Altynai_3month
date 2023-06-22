# HW 2
# 1 Построить архитектуру как на уроке !
# 2 К викторинам, которые уже существуют, добавить Callback (очередность вопросов с помощью кнопок)
# Ответов должно быть по 3 продолжения (добавить третий вопрос викторины) !
# 3 Закреплять сообщение при команде "!pin", только если это будет ответом на сообщение !
# 4 Если сообщение начинается на game, пусть бот отправляет рандомный анимированный эмоджи !
# Должно работать только для Админа


from aiogram import executor
import logging
from config import dp
from handlers import commands, callback, extra, admin

commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
