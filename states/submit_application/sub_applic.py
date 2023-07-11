from aiogram.dispatcher.filters.state import State, StatesGroup


class NewJoySubmitApplication(StatesGroup):
    first_name = State()
    phone_number = State()
