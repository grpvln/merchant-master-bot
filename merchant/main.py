import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5343770240:AAENia16rfGXXS6oFe468flSTtKsoywPl7c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
