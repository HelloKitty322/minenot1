import asyncio
from aiogram import Bot, Dispatcher

import answers
import config


async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(answers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
