import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from env import API_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start', state='*')
async def _(message: Message, state: FSMContext):
    state.update_data({'user_id': message.from_user.id})
    await message.answer('Привет, Напиши мне что нибудь!')
    await state.set_state('wait')

@dp.message_handler(state='wait')
async def _(message: Message, state: FSMContext):
    id2  = message.from_user.id
    text = f"@{message.from_user.username} написал(а):\n message.text"

    await message.answer(text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())
