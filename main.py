import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import start
from config import TOKEN
from database.crud import init_db

logging.basicConfig(level=logging.INFO)



async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(start.router)

    init_db
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
