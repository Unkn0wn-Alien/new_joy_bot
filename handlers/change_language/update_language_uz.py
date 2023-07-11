from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp, db

from states.change_language.change_language_uz import NewJoyChangeLanguage

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_ru


@dp.message_handler(state=NewJoyChangeLanguage.change_language, text="🇷🇺 Русский")
async def change_to_ru(message: types.Message, state: FSMContext):
    language = message.text.split(" ")[1]
    await db.update_user_language(language_user=language, telegram_id=message.from_user.id)
    await message.answer("Выберите действие 👇", reply_markup=sokin_diyor_ru)
    await state.finish()
