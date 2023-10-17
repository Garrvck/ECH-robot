from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher import FSMContext
import sqlite3
from keyboards.default.keyboards import Keyboard_month, Keyboard
from loader import dp, bot
from data.config import ADMINS
from states.menu_state import MenuState
from data.data import viks_sentabr, ppr_sentabr, sklad_sentabr, ppr_avgust, viks_avgust, sklad_avgust

@dp.message_handler(text="🔙 Orqaga", state='*')
async def Back(message: Message, state: FSMContext):
    await message.answer(text="Bosh menu", reply_markup=Keyboard)
    await state.finish()

@dp.message_handler(text="VIKS")
async def Viks(message: Message):
    await message.answer(text="VIKS vagonida aniqlangan kamchiliklar hisoboti", reply_markup=Keyboard_month)
    await MenuState.viks.set()

@dp.message_handler(text="SKLAD")
async def Sklad(message: Message):
    await message.answer(text="Korxona omboridagi materiallar", reply_markup=Keyboard_month)
    await MenuState.sklad.set()

@dp.message_handler(text="PPR")
async def Ppr(message: Message):
    await message.answer(text="Elektr qurilmalarini sinovdan o'tkazish nazorati", reply_markup=Keyboard_month)
    await MenuState.ppr.set()


@dp.message_handler(text="Sentabr", state=MenuState.viks)
async def Vikssentabr(msg: Message, state: FSMContext):
    await msg.answer_document(document=viks_sentabr)

@dp.message_handler(text="Sentabr", state=MenuState.sklad)
async def Skladsentabr(msg: Message, state: FSMContext):
    await msg.answer_document(document=sklad_sentabr)

@dp.message_handler(text="Sentabr", state=MenuState.ppr)
async def Pprsentabr(msg: Message, state: FSMContext):
    await msg.answer_document(document=ppr_sentabr)


@dp.message_handler(text="Avgust", state=MenuState.viks)
async def Vikssentabr(msg: Message, state: FSMContext):
    await msg.answer_document(document=viks_avgust)

@dp.message_handler(text="Avgust", state=MenuState.sklad)
async def Skladsentabr(msg: Message, state: FSMContext):
    await msg.answer_document(document=sklad_avgust)

@dp.message_handler(text="Avgust", state=MenuState.ppr)
async def Pprsentabr(msg: Message, state: FSMContext):
    await msg.answer_document(document=ppr_avgust)
