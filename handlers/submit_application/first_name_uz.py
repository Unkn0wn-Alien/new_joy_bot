from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp

from states.submit_application.sub_applic import NewJoySubmitApplication

from keyboards.default_keyboards.sokin_diyor_menu import sokin_diyor_menu_uz
from keyboards.default_keyboards.phone_number import phone_number_uz


@dp.message_handler(state=NewJoySubmitApplication.first_name, content_types=types.ContentTypes.TEXT)
async def sub_applast_name(message: types.Message, state: FSMContext):
    if message.text == "⬅ Ortga":
        await message.answer("Harakatni tanlang 👇", reply_markup=sokin_diyor_menu_uz)
        await state.finish()
    else:
        await state.update_data(first_name=message.text)
        await message.answer("Iltimos telefon raqamingizni yuboring 👇", reply_markup=phone_number_uz)
        await NewJoySubmitApplication.phone_number.set()
