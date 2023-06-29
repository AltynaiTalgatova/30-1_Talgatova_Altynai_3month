import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from apscheduler.triggers.date import DateTrigger


async def hsk_test():
    photo = open("media/hsk.jpeg", "rb")
    for user in ADMINs:
        await bot.send_photo(
            chat_id=user,
            photo=photo,
            caption=f"Today is your day! You've got HSK test today!"
        )


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        hsk_test,
        DateTrigger(
            run_date=datetime.datetime(year=2023, month=8, day=8)
        )
    )

    scheduler.start()
