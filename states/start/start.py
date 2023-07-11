from aiogram.dispatcher.filters.state import State, StatesGroup


class NewJoy(StatesGroup):
    choose_language = State()
