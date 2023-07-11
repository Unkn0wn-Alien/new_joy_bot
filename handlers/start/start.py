from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db

from states.start.start import NewJoy

from keyboards.default_keyboards.language import select_language
from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_uz, sokin_diyor_ru


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = []
    telegram_ids = await db.select_telegram_id()
    language = await db.select_language(message.from_user.id)
    for telegram_id in telegram_ids:
        ids = telegram_id["telegram_id"]
        id.append(ids)
    if message.from_user.id in id and language["language"] == "O'zbek":
        await message.answer("Botimizga xush kelibsiz", reply_markup=sokin_diyor_uz)
    elif message.from_user.id in id and language["language"] == "Русский":
        await message.answer("Добро пожаловать в наш бот", reply_markup=sokin_diyor_ru)
    else:
        await message.answer("Assalomu aleykum! Botimizga xush kelibsiz!\nIltimos tilni tanlang 👇\n\n"
                            "Здравствуйте! Добро пожаловать в наш бот!\nПожалуйста выберите язык 👇",
                            reply_markup=select_language)
        await NewJoy.choose_language.set()
