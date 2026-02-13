import asyncio
import logging
from handlers.pdf import router as pdf_router




from aiogram import Bot, Dispatcher

from handlers import start, instagram
from config import TOKEN
from database.crud import init_db

logging.basicConfig(level=logging.INFO)



async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(start.router)
<<<<<<< HEAD
    dp.include_router(pdf_router)
=======
    dp.include_router(instagram.router)
>>>>>>> b592b54adbb5e1a19d5d65aa474ea21a539cb120

    init_db()
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())