import asyncpg

from datetime import datetime

from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp, db

from states.start.start import NewJoy

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_uz, sokin_diyor_ru


@dp.message_handler(state=NewJoy.choose_language, text=["🇺🇿 O'zbek", "🇷🇺 Русский"])
async def select_language(message: types.Message, state: FSMContext):
    await state.update_data(lang=message.text)
    data = await state.get_data()
    lang = data.get("lang")
    language = lang.split(" ")[1]
    if message.from_user.username != None:
        try:
            await db.add_user(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                language=language,
                created_at=datetime.now()
            )
        except asyncpg.exceptions.UniqueViolationError:
            await db.select_user(telegram_id=message.from_user.id)
    else:
        try:
            await db.add_user(
                telegram_id=message.from_user.id,
                username=None,
                language=language,
                created_at=datetime.now()
            )
        except asyncpg.exceptions.UniqueViolationError:
            await db.select_user(telegram_id=message.from_user.id)
    if language == "O'zbek":
        await message.answer("Botimizga xush kelibsiz", reply_markup=sokin_diyor_uz)
    if language == "Русский":
        await message.answer("Добро пожаловать в наш бот", reply_markup=sokin_diyor_ru)
    await state.finish()
