from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_uz = KeyboardButton("🇺🇿 O'zbek")
language_ru = KeyboardButton("🇷🇺 Русский")
back_uz = KeyboardButton("⬅ Ortga")
back_ru = KeyboardButton("⬅ Назад")
select_language = ReplyKeyboardMarkup(resize_keyboard=True).row(language_uz, language_ru)
change_lan_uz = ReplyKeyboardMarkup(resize_keyboard=True).row(language_uz, language_ru).row(back_uz)
change_lan_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(language_uz, language_ru).row(back_ru)
