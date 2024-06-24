from aiogram.dispatcher.filters.state import State, StatesGroup

class set_ban(StatesGroup):
    id = State()
    name = State()

class set_unban(StatesGroup):
    name = State()

class plba(StatesGroup):
    rassulka = State()