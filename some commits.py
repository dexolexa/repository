# нужные библиотеки
import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message

from aiogram.utils.callback_data import CallbackData


from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from env import API_TOKEN

# логи
logging.basicConfig(level=logging.INFO)

# сам бот
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# кнопки

inb_callback_data = CallbackData('inb', 'purpose')

inb1 = InlineKeyboardButton("(работа или/и игры)пк", url="https://www.dns-shop.ru/configurator/")
inb2 = InlineKeyboardButton("консоль(игры)", callback_data=inb_callback_data.new('consolekb'))
inb3 = InlineKeyboardButton("создание музыки, программирование...", url='https://www.dns-shop.ru/catalog/recipe/8ddf1df79c19c23d/macbook/')
inb4 = InlineKeyboardButton('ВР ШЛЕМЫ', callback_data=inb_callback_data.new('vrkb'))

nb3 = KeyboardButton(text="геолокация и контакт")
nb4 = KeyboardButton(text="помощь с выбором")

geoloc = KeyboardButton(text="контакт", request_contact=True)
contact = KeyboardButton(text="геолокация", request_location=True)
back = KeyboardButton(text="Вернуться?")

console1 = InlineKeyboardButton('Портативные', callback_data="pkb")
console2 = InlineKeyboardButton('Домашние', callback_data="hkb")

portative1 = InlineKeyboardButton("Nintendo Switch", url="https://www.dns-shop.ru/catalog/17a893cd16404e77/konsoli-nintendo-switch/?utm_referrer=https%3A%2F%2Fwww.google.com%2F")
portative2 = InlineKeyboardButton("плейстейшен вита", url="https://market.yandex.ru/product--igrovaia-pristavka-sony-playstation-vita-slim/11870312?glfilter=14871214%3A50907325_101878265698&text=sony%20psp%20vita%20%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C&cpa=1&cpc=YJNOdajMA5sg1hqRnGdy5NeJk5ZiuUwWuqmBAyULBVOKpLS2YZhsvHjCLU0x5XImjLPvl4WVMLARRcK12mT2cWoMM3JfTGK_cVB1XtHWVkMm3eV0fzMZ36H5q-vzxJhFKSbNCoUjfeiGsZglAil0PpvfEw0j4_lIpZT-uGsP0RyXaNXjy5FTvby6DNy9jCQjJ3Vrp-J-DZ1LFKTbBkiGH1QEurk0-4v1HMM4OXqdtdKHw1puQkw73na_8ssR7j47xZmC4gE1PPmvFU7pohxyHA%2C%2C&sku=101878265698&do-waremd5=cIMgsQCDhfPI1MyazjhUsw&resale_goods=resale_resale&resale_goods_condition=resale_excellent&nid=34948569")

ps5 = InlineKeyboardButton("Плейстейшен 5", url="https://www.dns-shop.ru/product/9d34c67bf698ed20/igrovaa-konsol-playstation-5/")
xbox_x = InlineKeyboardButton("иксбокс сериес икс", url="https://www.dns-shop.ru/product/de3881f3d7dfed20/igrovaa-konsol-microsoft-xbox-series-x/")

pc_vr = InlineKeyboardButton("PC VR", callback_data="pc_vrkb")
svr = InlineKeyboardButton("Standalone", callback_data='svrkb')

pico_vr = InlineKeyboardButton("pico4", url="https://www.dns-shop.ru/product/613824286565ed20/sistema-virtualnoj-realnosti-pico-4-belyj/")
meta_q = InlineKeyboardButton("meta quest", url="https://www.dns-shop.ru/product/5fd76980e7a6ed20/sistema-virtualnoj-realnosti-oculus-quest-2-belyj/")

v_index = InlineKeyboardButton("Valve Index", url="https://market.yandex.ru/product--shlem-vr-valve-index-vr-kit/617316014?sku=100815105789&cpa=1")
htc_v = InlineKeyboardButton("HTC VIVE", url="https://market.yandex.ru/product--shlem-vr-htc-vive-pro-2/1734775226?cpc=eC--icU8u3IIztTioXytlJHKVzzVFszFG5KrW_MCOyfSG-v8lHEi6jK_phZQw3XIarFYF0tNM-2Gjzp1N3r-LF8lgcDjzIpRoy_usRhm87lGIyJog5Y4lZnTHtRWzb78BmZENFw0HG0PNet-AHgBSTWBxDyTQ-_aXMfBIwSCIUY0eP49CBA8J-8hlKoAeuwsIzUK_bSXAStoRk1Jpodd5yQSnQTfUk4TWi887gJCVTki8i1uf0pxuxcBKfOC4q9T0XgdFZWQm3IkzkdgoWtEZA%2C%2C&sku=101640938729&offerid=UIjE0orGF7jejHh96Ta8Lw&cpa=1")
rift = InlineKeyboardButton("OCULUS RIFT", url="https://market.yandex.ru/product--shlem-vr-oculus-rift-cv1-touch/1732361942?cpc=uluWlvdfUKDp1kr3xrPoNT58_I3hQyUvuUh90VdlxMtwZFuhdkjCr9zeyYrbdNKRzmztbjfYytaqjXrErAZczdnnzj-mkRXX-EETSRb2Gskb40qBFSd0d0retHBwEkm_p6Zvo8oMaqHf_1DZLWgEn44qdr_7DoRwb8Ft3ZTvpKQ2poDKVT0nMtzhliULD5tW6XHnCwVvc9qJogUJ0lNKeJ-f6fGTt0R7uKd_jp4paB_wG8VZKWHg41kruI8DxI_J05OM5zy0m-Zotf1JDZkAEQ%2C%2C&from-show-uid=16866410153934339547006002&sku=100395913978&do-waremd5=_pp25uBhYH4_V70INwaYFA&sponsored=1&cpa=1")





# само нахождение кнопок

kb = InlineKeyboardMarkup(row_width=2).add(inb2).add(inb1).add(inb3).add(inb4)

consolekb = InlineKeyboardMarkup(row_width=1).add(console1).add(console2)

pkb = InlineKeyboardMarkup(row_width=1).add(portative1).add()

hkb = InlineKeyboardMarkup(row_width=1).add(ps5).add(xbox_x)

vrkb = InlineKeyboardMarkup(row_width=1).add(svr).add(pc_vr)

svrkb = InlineKeyboardMarkup(row_width=1).add(meta_q).add(pico_vr)

pc_vrkb = InlineKeyboardMarkup(row_width=0.5).add(v_index).add(htc_v).insert(rift)


replies = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(nb4).add(nb3)

gckb = ReplyKeyboardMarkup(resize_keyboard=True).insert(geoloc).insert(contact).add(back)


# принятие кнопок
@dp.callback_query_handler(inb_callback_data.filter(), state='*')
async def process_callback_button(callback_query: types.CallbackQuery, message: types.Message,  callback_data: dict, state: FSMContext):
    purpose = callback_data['purpose']
    await bot.answer_callback_query(callback_query.id, text=purpose)
    await state.set_state(purpose)
    # await message.answer(text='выбирай', reply_markup=purpose)

# основные функции
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



@dp.callback_query_handler(lambda c: c.data == 'back', state='*')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text='vr')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())
