import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message

from aiogram.dispatcher import FSMContext


from env import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

replies = ReplyKeyboardMarkup(resize_keyboard=True)

kb = InlineKeyboardMarkup(row_width=2)
inb1 = InlineKeyboardButton(text="какая-то ссылка на ютуб?", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
inb2 = InlineKeyboardButton(text="телега бота", url="t.me/really_shitty_bot")
inb3 = KeyboardButton(text="геолокация и контакт")
inb4 = KeyboardButton(text="помощь с выбором")
kb.add(inb2).add(inb1)  # .add(inb3).add(inb4)

replies.add(inb4).add(inb3)


async def on_startup():
    print("done!")


@dp.message_handler(commands=['start'], state="*")
async def f_c(message: types.Message, state: FSMContext):
    await message.answer(text='Что надо', reply_markup=replies)
    await state.set_state('ans')

exmp_l = ['>18', '<18']
@dp.message_handler(state='ans')
async def msg_r(message: types.Message):
    if message.text == '' or message.text == '>18':

        if message.text == '<18':
            await bot.send_message(message.from_user.id, text='розбийник! Уходи!')

        elif message.text == '>18':
            await bot.send_message(message.from_user.id, text='проходите!')
    else:
        None



# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())
