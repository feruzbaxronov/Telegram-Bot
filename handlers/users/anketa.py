from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personaldata import PersonalData

@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state:FSMContext):
    fullname=message.text
    await state.update_data(name=fullname)
    await message.answer("Email manzilingizni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state:FSMContext):
    email=message.text
    await state.update_data(
        {"email": email}
    )
    await message.answer("Telefon raqamingizni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phonenum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone=message.text
    await state.update_data(
        {"phone":phone}
    )

    data=await state.get_data()
    name=data.get("name")
    email=data.get("email")
    phone=data.get("phone")


    msg="Sizdan Quyidagi Ma'lumotlar Qabul Qilindi📝:\n"
    msg+=f"Ismingiz- {name}\n"
    msg+=f"Email💳:-    {email}\n"
    msg+=f"telefon☎:-{phone}"
    await message.answer(msg)
    await state.finish()
