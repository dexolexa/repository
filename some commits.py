"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from env import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!, what do you want?")
    button_echo = KeyboardButton('I want an echo bot!')
    button_no = KeyboardButton('Get yo shitty_bot ass outta here!!!')



@dp.message_handler()
async def echo(message: types.Message):



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)