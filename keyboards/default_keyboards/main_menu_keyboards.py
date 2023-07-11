from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sok_diy_uz = KeyboardButton("TJM Sokin Diyor")
sok_diy_ru = KeyboardButton("ЖК Sokin Diyor")
change_lang_uz = KeyboardButton("🌏 Tilni o'zgartirish")
change_lang_ru = KeyboardButton("🌏 Изменить язык")
sokin_diyor_uz = ReplyKeyboardMarkup(resize_keyboard=True).row(sok_diy_uz, change_lang_uz)
sokin_diyor_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(sok_diy_ru, change_lang_ru)
