# нужные библиотеки
import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from env import API_TOKEN

# логи
logging.basicConfig(level=logging.INFO)

# сам бот
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


#кнопки

inb1 = InlineKeyboardButton("(работа или/и игры)пк", callback_data='pc')
inb2 = InlineKeyboardButton("консоль(игры)", callback_data='cons')
inb3 = InlineKeyboardButton("создание музыки, программирование...", callback_data='mac')
inb4 = InlineKeyboardButton('ВР ШЛЕМЫ', callback_data='vrhelm')

nb3 = KeyboardButton(text="геолокация и контакт")
nb4 = KeyboardButton(text="помощь с выбором")

geoloc = KeyboardButton(text="контакт", request_contact=True)
contact = KeyboardButton(text="геолокация", request_location=True)
contact2 = KeyboardButton(text="Вернуться?")

# console1 = InlineKeyboardButton('Портативные',callback_data="port")
# console2 = InlineKeyboardButton('Домашние',callback_data="home")
#
# portative1 = InlineKeyboardButton("Nintendo Switch", url="")
# portative2 = InlineKeyboardButton("", url="")
#
# ps5 = InlineKeyboardButton("", url="")
# xbox_x = InlineKeyboardButton("", url="")
#
# vr_s = InlineKeyboardButton("", url="")
# pc_vr = InlineKeyboardButton("", url="")
#
# pico_vr = InlineKeyboardButton("", url="")
# meta_q = InlineKeyboardButton("", url="")
#
# v_index = InlineKeyboardButton("", url="")
# htc_v = InlineKeyboardButton("", url="")
# rift = InlineKeyboardButton("", url="")
#
# macbook = InlineKeyboardButton('макбук', url="https://www.dns-shop.ru/catalog/recipe/8ddf1df79c19c23d/macbook/")
#
# gamingpc = InlineKeyboardButton("", url="")
#
# gamingandworkin = InlineKeyboardButton("", url="")
#
# workinpc = InlineKeyboardButton("", url="")


# само нахождение кнопок

kb = InlineKeyboardMarkup(row_width=2).add(inb2).add(inb1).add(inb3).add(inb4)

# consolekb = InlineKeyboardMarkup(row_width=1).add(console1).add(console2)

# pkb = InlineKeyboardMarkup(row_width=1).add().add()

# hkb = InlineKeyboardMarkup(row_width=1).add().add()

# vrkb = InlineKeyboardMarkup(row_width=1).add(vr_s).add(pc_vr)

# svr=InlineKeyboardMarkup(row_width=1).add().add(pico_vr)

# macbookkb = InlineKeyboardMarkup(row_width=1).add(macbook)

# pckb = InlineKeyboardMarkup(row_width=1).add(gamingpc).add(workinpc).add(gamingandworkin)


replies = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(nb4).add(nb3)

gckb= ReplyKeyboardMarkup(resize_keyboard=True).insert(geoloc).insert(contact).add(contact2)


# принятие кнопок
@dp.callback_query_handler(lambda c: c.data == 'pc', state ='*')
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id, text='pc')
    await state.set_state('choicepc')
    # await message.answer(text='Что выбираешь и для чего?', reply_markup=kb)
@dp.callback_query_handler(lambda c: c.data == 'mac', state="*")
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id, text='mac')
    await state.set_state('mac')
    # await message.answer(text='Тебе нужен мак!(если деньги есть...)', reply_markup=kb)
@dp.callback_query_handler(lambda c: c.data == 'cons', state='*')
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
     await bot.answer_callback_query(callback_query.id, text='console')
     await state.set_state('console')
     # await message.answer(text='Какой тип консоли?', reply_markup=kb)
@dp.callback_query_handler(lambda c: c.data == 'vrhelm',state="*")
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id, text='vr')
    state.set_state("vr")
    # await message.answer(text='', reply_markup=kb)
#основные функции
async def on_startup():
    print("done!")

# @dp.message_handler(commands=['clear'], state='*')
# async def clear(message: types.message):
#     replies = types.ReplyKeyboardRemove()
#     gckb = types.ReplyKeyboardRemove()

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
    if message.text == 'помощь с выбором':
        await state.set_state('choice')
        await message.answer(text='Что выбираешь и для чего?', reply_markup=kb)
    elif message.text == 'геолокация и контакт':
        await state.set_state('geo')
        await message.answer(text='Выбирай', reply_markup=gckb)


@dp.message_handler(state='geo')
async def geo_cont(message: types.Message, state: FSMContext):
    if message.text == 'Вернуться?':
        await state.set_state('ans')
        await message.answer(text='Что надо', reply_markup=replies)
    else:
        pass


# @dp.message_handler(state='vr')
# async def choice(message: types.message, state: FSMContext):
# @dp.callback_query_handler(lambda c: c.data == 'back', state='*')
# async def process_callback_button(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id, text='vr')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())
