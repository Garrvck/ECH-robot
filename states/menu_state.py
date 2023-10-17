from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuState(StatesGroup):
    viks = State()
    sklad = State()
    ppr = State()