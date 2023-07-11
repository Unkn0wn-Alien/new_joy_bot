from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_uz = KeyboardButton("⬅ Ortga")
back_ru = KeyboardButton("⬅ Назад")
back_btn_uz = ReplyKeyboardMarkup(resize_keyboard=True).row(back_uz)
back_btn_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(back_ru)
