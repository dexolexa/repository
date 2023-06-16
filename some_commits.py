'''Import asyncio and other important libraries.'''
import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message
from aiogram.utils.callback_data import CallbackData



from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from env import API_TOKEN

'''Configure logging'''
logging.basicConfig(level=logging.INFO)

'''Configure bot & dispatcher'''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


'''Callback data for buttons'''
inb_callback_data = CallbackData('inb', 'purpose')
'''choice for pc or mac, console or vr.'''
pcb = InlineKeyboardButton("Pc", callback_data=inb_callback_data.new('pc'))
conb = InlineKeyboardButton("Console", callback_data=inb_callback_data.new('consolekb'))
macb = InlineKeyboardButton("Macbook", url='https://www.dns-shop.ru/catalog/recipe/8ddf1df79c19c23d/macbook/')
vrb = InlineKeyboardButton('Vr helmets', callback_data=inb_callback_data.new('vrkb'))
'''1st Choice '''
nb3 = KeyboardButton(text="geolocation and contact")
nb4 = KeyboardButton(text="Help me choose a option.")
'''geolocations & back buttons'''
geoloc = KeyboardButton(text="contact", request_contact=True)
contact = KeyboardButton(text="geolocation(works only on a phone!)", request_location=True)
back = InlineKeyboardButton(text="back", callback_data=inb_callback_data.new("back"))
backm = InlineKeyboardButton(text="back to menu", callback_data=inb_callback_data.new("menu"))
'''console type'''
consoleport = InlineKeyboardButton('Portative', callback_data=inb_callback_data.new("pkb"))
consolehome = InlineKeyboardButton('Home systems', callback_data=inb_callback_data.new("hkb"))
'''portable consoles'''
Nintendo = InlineKeyboardButton("Nintendo Switch", url="https://www.dns-shop.ru/catalog/17a893cd16404e77/konsoli-nintendo-switch/?utm_referrer=https%3A%2F%2Fwww.google.com%2F")
PSV = InlineKeyboardButton("Playstation vita", url="https://market.yandex.ru/product--igrovaia-pristavka-sony-playstation-vita-slim/11870312?glfilter=14871214%3A50907325_101878265698&text=sony%20psp%20vita%20%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C&cpa=1&cpc=YJNOdajMA5sg1hqRnGdy5NeJk5ZiuUwWuqmBAyULBVOKpLS2YZhsvHjCLU0x5XImjLPvl4WVMLARRcK12mT2cWoMM3JfTGK_cVB1XtHWVkMm3eV0fzMZ36H5q-vzxJhFKSbNCoUjfeiGsZglAil0PpvfEw0j4_lIpZT-uGsP0RyXaNXjy5FTvby6DNy9jCQjJ3Vrp-J-DZ1LFKTbBkiGH1QEurk0-4v1HMM4OXqdtdKHw1puQkw73na_8ssR7j47xZmC4gE1PPmvFU7pohxyHA%2C%2C&sku=101878265698&do-waremd5=cIMgsQCDhfPI1MyazjhUsw&resale_goods=resale_resale&resale_goods_condition=resale_excellent&nid=34948569")
'''home entertinament'''
ps5 = InlineKeyboardButton("PS5", url="https://www.dns-shop.ru/product/9d34c67bf698ed20/igrovaa-konsol-playstation-5/")
xbox_x = InlineKeyboardButton("Xbox series X", url="https://www.dns-shop.ru/product/de3881f3d7dfed20/igrovaa-konsol-microsoft-xbox-series-x/")
'''vr types'''
pc_vr = InlineKeyboardButton("PC VR", callback_data=inb_callback_data.new("pc_vrk"))
svr = InlineKeyboardButton("Standalone", callback_data=inb_callback_data.new('svrk'))
'''standalone vr, not dependent on pc'''
pico_vr = InlineKeyboardButton("pico4", url="https://www.dns-shop.ru/product/613824286565ed20/sistema-virtualnoj-realnosti-pico-4-belyj/")
meta_q = InlineKeyboardButton("meta quest", url="https://www.dns-shop.ru/product/5fd76980e7a6ed20/sistema-virtualnoj-realnosti-oculus-quest-2-belyj/")
'''pc vr, dependent on pc'''
v_index = InlineKeyboardButton("Valve Index(needs a good pc like a 3060rtx)", url="https://market.yandex.ru/product--shlem-vr-valve-index-vr-kit/617316014?sku=100815105789&cpa=1")
htc_v = InlineKeyboardButton("HTC VIVE(needs a 2060)", url="https://market.yandex.ru/product--shlem-vr-htc-vive-pro-2/1734775226?cpc=eC--icU8u3IIztTioXytlJHKVzzVFszFG5KrW_MCOyfSG-v8lHEi6jK_phZQw3XIarFYF0tNM-2Gjzp1N3r-LF8lgcDjzIpRoy_usRhm87lGIyJog5Y4lZnTHtRWzb78BmZENFw0HG0PNet-AHgBSTWBxDyTQ-_aXMfBIwSCIUY0eP49CBA8J-8hlKoAeuwsIzUK_bSXAStoRk1Jpodd5yQSnQTfUk4TWi887gJCVTki8i1uf0pxuxcBKfOC4q9T0XgdFZWQm3IkzkdgoWtEZA%2C%2C&sku=101640938729&offerid=UIjE0orGF7jejHh96Ta8Lw&cpa=1")
rift = InlineKeyboardButton("OCULUS RIFT(needs a 1660)", url="https://market.yandex.ru/product--shlem-vr-oculus-rift-cv1-touch/1732361942?cpc=uluWlvdfUKDp1kr3xrPoNT58_I3hQyUvuUh90VdlxMtwZFuhdkjCr9zeyYrbdNKRzmztbjfYytaqjXrErAZczdnnzj-mkRXX-EETSRb2Gskb40qBFSd0d0retHBwEkm_p6Zvo8oMaqHf_1DZLWgEn44qdr_7DoRwb8Ft3ZTvpKQ2poDKVT0nMtzhliULD5tW6XHnCwVvc9qJogUJ0lNKeJ-f6fGTt0R7uKd_jp4paB_wG8VZKWHg41kruI8DxI_J05OM5zy0m-Zotf1JDZkAEQ%2C%2C&from-show-uid=16866410153934339547006002&sku=100395913978&do-waremd5=_pp25uBhYH4_V70INwaYFA&sponsored=1&cpa=1")
'''types of pc's'''
pc_gaming = InlineKeyboardButton("Gaming pc", url="https://www.dns-shop.ru/product/d0e984868035ed20/pk-ardor-gaming-rage-h292/")
pc_working = InlineKeyboardButton("Pc for work", url="https://www.dns-shop.ru/product/c2fa829b664ced20/mini-pk-dexp-mini-entry-i002/")





'''choices between pc, vr, mac, console...'''
choicekb = InlineKeyboardMarkup(row_width=2).add(pcb).add(macb).add(vrb).add(conb).add(backm)

consolekb = InlineKeyboardMarkup(row_width=1).add(consoleport).add(consolehome).add(back)

portkb = InlineKeyboardMarkup(row_width=1).add(Nintendo).add(PSV).add(back)

homekb = InlineKeyboardMarkup(row_width=1).add(ps5).add(xbox_x).add(back)

vrkb = InlineKeyboardMarkup(row_width=1).add(svr).add(pc_vr).add(back)

s_vrkb = InlineKeyboardMarkup(row_width=1).add(meta_q).add(pico_vr).add(back)

pc_vrkb = InlineKeyboardMarkup(row_width=0.5).add(v_index).add(htc_v).insert(rift).add(back)

pcs = InlineKeyboardMarkup(row_width=0.5).add(pc_working).insert(pc_gaming).add(back)

replies = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(nb4).add(nb3)

geocontkb = ReplyKeyboardMarkup(resize_keyboard=True).insert(geoloc).insert(contact).add(back)


'''callback reciever'''
@dp.callback_query_handler(inb_callback_data.filter(), state='*')
async def process_callback_button(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    purpose = callback_data['purpose']
    await bot.answer_callback_query(callback_query.id)
    if purpose == 'vrkb':

        await bot.send_message(chat_id=callback_query.from_user.id, text='What type of Vr do you need?', reply_markup=vrkb)
    elif purpose == 'consolekb':

        await bot.send_message(chat_id=callback_query.from_user.id, text='What type of console do you need?', reply_markup=consolekb)
    elif purpose == 'pkb':

        await bot.send_message(chat_id=callback_query.from_user.id, text='What console do you need?', reply_markup=portkb)
    elif purpose == 'hkb':

        await bot.send_message(chat_id=callback_query.from_user.id, text='What console do you need?', reply_markup=homekb)
    elif purpose == "svrk":

        await bot.send_message(chat_id=callback_query.from_user.id, text='What type of vr do you need?', reply_markup=s_vrkb)
    elif purpose == 'pc_vrk':

        await bot.send_message(chat_id=callback_query.from_user.id, text='What type of vr do you need?', reply_markup=pc_vrkb)
    elif purpose == "back":

        await bot.send_message(chat_id=callback_query.from_user.id, text='What do you need?', reply_markup=choicekb)
    elif purpose == "menu":
        await state.set_state("ans")

        await bot.send_message(chat_id=callback_query.from_user.id, text='Going back...', reply_markup=replies)
        await asyncio.sleep(5)
    elif purpose == "pc":
        await bot.send_message(chat_id=callback_query.from_user.id, text='What pc do you need?', reply_markup=pcs)



'''main functions'''
async def on_startup():
    print("done!")

'''start!'''
@dp.message_handler(commands=['start'], state="*")
async def f_c(message: types.Message, state: FSMContext):
    await message.answer(text='What do you need?', reply_markup=replies)
    await state.set_state('ans')

'''options'''
@dp.message_handler(state='ans')
async def msg_r(message: types.Message, state: FSMContext):
    if message.text == 'Help me choose a option.':
        await state.set_state('choice')
        await message.answer(text='What do you need?', reply_markup=choicekb)

    elif message.text == 'geolocation and contact':
        await state.set_state('geo')
        await message.answer(text='Choose', reply_markup=geocontkb)

'''geolocation & contacts'''
@dp.message_handler(state='geo')
async def geo_cont(message: types.Message, state: FSMContext):
    if message.text == 'back':
        await state.set_state('ans')
        await message.answer(text='What do you need?', reply_markup=replies)
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=())
