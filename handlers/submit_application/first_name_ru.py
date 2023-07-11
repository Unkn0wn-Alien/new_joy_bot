from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp

from states.submit_application.sub_application import NewjoySubmitApplication

from keyboards.default_keyboards.sokin_diyor_menu import sokin_diyor_menu_ru
from keyboards.default_keyboards.phone_number import phone_number_ru


@dp.message_handler(state=NewjoySubmitApplication.first_name, content_types=types.ContentTypes.TEXT)
async def sub_applast_name(message: types.Message, state: FSMContext):
    if message.text == "⬅ Назад":
        await message.answer("Выберите действие 👇", reply_markup=sokin_diyor_menu_ru)
        await state.finish()
    else:
        await state.update_data(first_name=message.text)
        await message.answer("Пожалуйста отправьте ваш телефон номер 👇", reply_markup=phone_number_ru)
        await NewjoySubmitApplication.phone_number.set()
