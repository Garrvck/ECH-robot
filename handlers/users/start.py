from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.keyboards import Keyboard
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(text=f"Xush kelibsiz!", reply_markup=Keyboard)
    #Termiz elektr ta'minoti korxonasi
