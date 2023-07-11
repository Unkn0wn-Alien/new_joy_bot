from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp

from states.change_language.change_language_uz import NewJoyChangeLanguage

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_uz


@dp.message_handler(state=NewJoyChangeLanguage.change_language, text="⬅ Ortga")
async def back_settings(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanglang 👇", reply_markup=sokin_diyor_uz)
    await state.finish()
