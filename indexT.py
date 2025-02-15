import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7874655600:AAHGOx9RIoGujY4HDTiTrgUycZK0nNPGe6c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я твой Telegram-бот 🤖")

@dp.message(Command("play"))
async def play_rps(message: Message):
    options = ['Камень', 'Ножницы', 'Бумага']
    user_choice = message.get_args().capitalize()
    if user_choice not in options:
        await message.answer("Пожалуйста, выбери одно из: Камень, Ножницы, Бумага.")
        return

    bot_choice = random.choice(options)

    if user_choice == bot_choice:
        result = 'Ничья!'
    elif (user_choice == 'Камень' and bot_choice == 'Ножницы') or \
         (user_choice == 'Ножницы' and bot_choice == 'Бумага') or \
         (user_choice == 'Бумага' and bot_choice == 'Камень'):
        result = 'Ты победил!'
    else:
        result = 'Я победил!'

    response = f'Ты выбрал {user_choice}, я выбрал {bot_choice}. {result}'
    await message.answer(response)

@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("Я тебе не буду помогать 🤖")

async def main():
    print("бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
