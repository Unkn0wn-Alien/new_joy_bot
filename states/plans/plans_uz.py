from aiogram.dispatcher.filters.state import State, StatesGroup


class NewJoyPlan(StatesGroup):
    quantity_complexes = State()
