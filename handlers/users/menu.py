from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.manuKeyboard import menu
from keyboards.default.pythonKeyboards import menuPython

from loader import dp
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Assalomu alaykum \n Bexruz Baxronovning sahifasiga xush kelipsiz", reply_markup=menu)


@dp.message_handler(text="Bexruz Baxronov")
async def send_link(message: Message):
    await message.answer("Baxronov Bexruzning sahifalari", reply_markup=menuPython)

@dp.message_handler(text="GitHub sahifamiz")
async def send_link(message: Message):
    await message.answer("Bexruz Baxronov Github sahifasi: https://github.com/bexruz5113", reply_markup=menuPython)

@dp.message_handler(text="Telegram orqali bog'lanish")
async def send_link(message: Message):
    await message.answer("Bexruz Baxronov telegram sahifasi:https://t.me/bexruz_baxronov", reply_markup=menuPython)

@dp.message_handler(text="Instagram sahifamiz")
async def send_link(message: Message):
    await message.answer("Bexruz Baxronov instagram sahifasi:EMPTY", reply_markup=menuPython)


@dp.message_handler(text="ortga")
async def send_link(message: Message):
    await message.answer(message.answer("Assalomu alaykum \n Bexruz Baxronovning sahifasiga xush kelipsiz", reply_markup=menu))

