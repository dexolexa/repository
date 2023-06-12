import logging
from typing import Iterable, Optional

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils import executor
from dataclasses import dataclass, field

from env import TOKEN


@dataclass
class Dialog:
    name: str
    users: Optional[set[int]] = field(default_factory=lambda: set())

    def not_me(self, me: int) -> set[int]:
        return self.users - {me}

    def add_user(self, user_id: int):
        self.users.add(user_id)

    def remove_user(self, user_id: int):
        self.users.remove(user_id)

    def __str__(self):
        return f"{self.name} ({len(self.users)})"


# Настройа логгирования
logging.basicConfig(level=logging.INFO)

# Инициализировать бота и задать диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

all_users = set()

dialogs: list[Dialog] = []


@dp.message_handler(commands=['start'], state="*")
async def _(message: Message, state: FSMContext):
    user_id = message.from_id

    # Запоминаем всех пользователей, что нажали /start
    if user_id not in all_users:
        all_users.add(user_id)
        await send_to_users(f"Всего пользователей: {len(all_users)}")

    await state.update_data({"user_id": user_id,
                             "username": message.from_user.username})
    await message.answer("Привет! Напиши мне что-нибудь!")
    # то же самое что и
    # await bot.send_message(message.from_id, "Привет! Напиши мне что-нибудь!")
    await state.set_state("list_dialogs")


@dp.message_handler(state="list_dialogs")
async def _(message: Message, state: FSMContext):
    await list_dialogs(message)
    await state.set_state("setup_dialog")


async def list_dialogs(message: Message):
    text = "Текущие диалоги: "
    text += ",".join(map(str, dialogs))
    await message.answer(text)
    await message.answer("Выберите нужный диалог (напишите его имя, либо 'new' )")


@dp.message_handler(state="setup_dialog")
async def _(message: Message, state: FSMContext):
    name_of_dialog = message.text.strip()

    if name_of_dialog == 'new':
        await message.answer("Введите название для диалога")
        await state.set_state("create_dialog")
        return
    elif name_of_dialog == 'update':
        await list_dialogs(message)

    chosen_dialog = None

    for dialog in dialogs:
        if name_of_dialog == dialog.name:
            chosen_dialog = dialog
            break

    if chosen_dialog:
        await message.answer(f"Вы выбрали диалог: {chosen_dialog}")
        await chose_dialog(message.from_id, chosen_dialog)
        await state.update_data({"dialog": chosen_dialog})
        await state.set_state("wait_for_message")
    else:
        await message.answer("Вы не ввели существующего диалога")
        await list_dialogs(message)


async def chose_dialog(user_id: int, chosen_dialog: Dialog):
    text = f"Пользователь {user_id} вышел из этого диалога."
    for dialog in dialogs:
        if dialog is chosen_dialog:
            continue
        if user_id in dialog.users:
            dialog.remove_user(user_id)
            await send_to_users(text, dialog.users)

    chosen_dialog.add_user(user_id)
    text = f"Пользователь {user_id} добавился в этот диалог."
    await send_to_users(text, chosen_dialog.not_me(user_id))


@dp.message_handler(state="create_dialog")
async def _(message: Message, state: FSMContext):
    name_of_dialog = message.text
    new_dialog = Dialog(name=name_of_dialog)
    dialogs.append(new_dialog)
    await chose_dialog(message.from_id, new_dialog)
    await message.answer(f"Вы создали новый диалог {new_dialog}. Вы находитесь в нём")
    await state.update_data({"dialog": new_dialog})
    await state.set_state("wait_for_message")


@dp.message_handler(state="wait_for_message")
async def _(message: Message, state: FSMContext):
    # await message.answer("Спасибо за сообщение!")
    # id_ = message.from_id # постоянный для аккаунта
    # message.from_user.username # пользователь может сменить его
    # text = f"@{message.from_user.username} написал(а):\n{message.text}"

    text = \
        f"<a href='tg://user?id={message.from_id}'>" \
        f"пользователь</a> написал(а):\n{message.text}"

    my_data = await state.get_data()
    dialog = my_data['dialog']
    if not dialog:
        await message.answer("Вы не находитесь в диалоге")
    all_except_me = dialog.not_me(message.from_id)
    await send_to_users(text, users=all_except_me, parse_mode="HTML")

    # await message.answer(text, parse_mode="HTML")


async def send_to_users(text, users: Iterable[int] = None, parse_mode=None):
    if users is None:
        users = tuple(all_users)
    else:
        users = tuple(users)

    for user_id in users:
        await bot.send_message(user_id, text, parse_mode=parse_mode)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)