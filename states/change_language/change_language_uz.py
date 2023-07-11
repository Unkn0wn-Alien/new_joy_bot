from aiogram.dispatcher.filters.state import State, StatesGroup


class NewJoyChangeLanguage(StatesGroup):
    change_language = State()