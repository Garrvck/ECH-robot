from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

back = KeyboardButton(text="🔙 Orqaga")

Keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="VIKS")],[
        KeyboardButton(text="SKLAD")],[
        KeyboardButton(text="PPR")
    ]],
    resize_keyboard=True
)


Keyboard_month = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Sentabr")],[
        KeyboardButton(text="Avgust")
    ]],
    resize_keyboard=True
)
Keyboard_month.row()
Keyboard_month.insert(back)
