import asyncio
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from weatherapp import get_weather


TOKEN =("7874655600:AAHGOx9RIoGujY4HDTiTrgUycZK0nNPGe6c")

bot = Bot(token=TOKEN)
dp = Dispatcher()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start"), KeyboardButton(text="/help")],
        [KeyboardButton(text="/play Камень"), KeyboardButton(text="/play Ножницы"), KeyboardButton(text="/play Бумага")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я твой Telegram-бот 🤖\nВыбери команду ниже:", reply_markup=keyboard)

@dp.message(Command("play"))
async def play_rps(message: Message):
    options = ['Камень', 'Ножницы', 'Бумага']

    args = message.text.split()
    if len(args) < 2:
        await message.answer("Пожалуйста, введи свой выбор после команды: /play Камень")
        return

    user_choice = args[1].capitalize()

    if user_choice not in options:
        await message.answer("Неправильный выбор. Доступные варианты: Камень, Ножницы, Бумага.")
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

    await message.answer(f'Ты выбрал {user_choice}, я выбрал {bot_choice}. {result}')

@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("Я тебе помогу! Вот доступные команды:\n"
                         "/start - Запустить бота\n"
                         "/play [Камень/Ножницы/Бумага] - Сыграть в игру\n"
                         "/help - Получить помощь")

@dp.message(Command("weather"))
async def send_weather(message:Message):
    weather_info = await get_weather()
    await message.reply(weather_info)


async def main():
    print("Бот запущен 🚀")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
