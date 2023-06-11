import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from env import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

replies = ReplyKeyboardMarkup(resize_keyboard=True)

kb = InlineKeyboardMarkup(row_width=2)
inb1 = InlineKeyboardButton("(работа или/и игры)пк", callback_data='b1')
inb2 = InlineKeyboardButton("консоль(игры)", callback_data='b2')
inb3 = InlineKeyboardButton("создание музыки, программирование...", callback_data='b3')
inb4 = InlineKeyboardButton("Vr шлем", callback_data='b4')
nb3 = KeyboardButton(text="геолокация и контакт")
nb4 = KeyboardButton(text="помощь с выбором")
kb.add(inb2).add(inb1)  # .add(inb3).add(inb4)
geoloc = KeyboardButton(text="контакт", request_contact=True)
contact = KeyboardButton(text="геолокация", request_location=True)
contact2 = KeyboardButton(text="Вернуться?", callback_data='back')
gckb= ReplyKeyboardMarkup(resize_keyboard=True).insert(geoloc).insert(contact)

replies.add(nb4).add(nb3)


async def on_startup():
    print("done!")


@dp.message_handler(commands=['start'], state="*")
async def f_c(message: types.Message, state: FSMContext):
    # try:
    #     gckb = types.ReplyKeyboardRemove()
    #     replies = types.ReplyKeyboardRemove()
    # except:
    #     await message.answer(text='Что надо', reply_markup=replies)

    await message.answer(text='Что надо', reply_markup=replies)
    await state.set_state('ans')

@dp.message_handler(state='ans')
async def msg_r(message: types.Message, state: FSMContext):

    if message.text == 'геолокация и контакт' or message.text == 'помощь с выбором':

        if message.text == 'помощь с выбором':
            await state.set_state('choice')

        elif message.text == 'геолокация и контакт':
            await state.set_state('geo')
    else:
        None

@dp.message_handler(state='geo')
async def geo_cont(message: types.Message, state: FSMContext):
    replies = types.ReplyKeyboardRemove()
    await message.answer(text='Выбирай',reply_markup=gckb)
    if message.text == 'Вернуться?':
        await state.set_state('ans')
    else:
        pass


@dp.message_handler(state='choice')
async def choice(message: types.message, state: FSMContext):
    await message.answer(text='Что выбираешь и для чего?', reply_markup=kb)




@dp.callback_query_handler(lambda callback: callback.data == 'b2',state="*")
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id


@dp.callback_query_handler(lambda c: c.data == 'b1',state='*')
async def process_callback_button(callback_query: types.CallbackQuery,state: FSMContext):
    await bot.send_message(callback_query.from_user.id)
    await bot.answer_callback_query(callback_query.id)
    await state.set_state('')

@dp.callback_query_handler(lambda callback: callback.data == 'b4', state="*")
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id


@ dp.callback_query_handler(lambda c: c.data == 'b3', state='*')
def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):

     await bot.send_message(callback_query.from_user.id)
     await bot.answer_callback_query(callback_query.id)
     await state.set_state('mac')

    @dp.callback_query_handler(lambda c: c.data == 'back', state='*')
    async def process_callback_button(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())
