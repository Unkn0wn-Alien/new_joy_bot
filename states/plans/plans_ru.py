from aiogram.dispatcher.filters.state import State, StatesGroup


class NewJoyplan(StatesGroup):
    quantity_complexes = State()
