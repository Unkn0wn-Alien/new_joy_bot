from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp

from states.change_language.change_language_ru import NewJoyChangelanguage

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_ru


@dp.message_handler(state=NewJoyChangelanguage.change_language, text="⬅ Назад")
async def back_settings(message: types.Message, state: FSMContext):
    await message.answer("Выберите действие 👇", reply_markup=sokin_diyor_ru)
    await state.finish()
