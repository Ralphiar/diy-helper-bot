import os, asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    text = (
        "Привет! Я бот-помощник по домашнему ремонту.\n"
        "Отправь фото поломки или текстовый вопрос — и я подскажу, что делать."
    )
    await message.answer(text)

async def main():
    # отключаем вебхуки, начинаем опрос (polling)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
