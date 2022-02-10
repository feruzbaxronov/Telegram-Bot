from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="GitHub sahifamiz"),
            KeyboardButton(text="Telegram orqali bog'lanish"),
            KeyboardButton(text="Instagram sahifamiz"),
        ],
        [
            KeyboardButton(text="ortga"),
            #KeyboardButton(text="Boshiga")
        ],
    ],
    resize_keyboard=True
)