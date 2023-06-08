

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Message

from env import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


kb = InlineKeyboardMarkup(row_width=2)
inb1 = InlineKeyboardButton(text="you", url="")
inb2 = InlineKeyboardButton(text="bot", url="")

async def on_startup():
    print("done!")

@df.message_handeler(commands=('f'))
async def f_c(message: types.Message):
    await message.anwser(text="надейся")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())