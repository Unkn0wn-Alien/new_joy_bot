from aiogram.dispatcher.filters.state import State, StatesGroup


class NewjoySubmitApplication(StatesGroup):
    first_name = State()
    phone_number = State()
