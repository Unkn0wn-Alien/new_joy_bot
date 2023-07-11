from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp, db

from states.change_language.change_language_ru import NewJoyChangelanguage

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_uz


@dp.message_handler(state=NewJoyChangelanguage.change_language, text="🇺🇿 O'zbek")
async def change_to_ru(message: types.Message, state: FSMContext):
    language = message.text.split(" ")[1]
    await db.update_user_language(language_user=language, telegram_id=message.from_user.id)
    await message.answer("Harakatni tanlang 👇", reply_markup=sokin_diyor_uz)
    await state.finish()
