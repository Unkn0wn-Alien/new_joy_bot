from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

leave_applict_uz = KeyboardButton("☎ Biz bilan bog'lanish")
one_uz = KeyboardButton("1-blok")
two_uz = KeyboardButton("2-blok")
three_uz = KeyboardButton("3-blok")
four_uz = KeyboardButton("4-blok")
five_uz = KeyboardButton("5-blok")
back_uz = KeyboardButton("⬅ Ortga")
leave_applict_ru = KeyboardButton("☎ Связаться с нами")
one_ru = KeyboardButton("1-блок")
two_ru = KeyboardButton("2-блок")
three_ru = KeyboardButton("3-блок")
four_ru = KeyboardButton("4-блок")
five_ru = KeyboardButton("5-блок")
back_ru = KeyboardButton("⬅ Назад")
complexes_uz = ReplyKeyboardMarkup(resize_keyboard=True).row(leave_applict_uz).row(one_uz, two_uz).row(three_uz,
    four_uz).row(five_uz).row(back_uz)
complexes_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(leave_applict_ru).row(one_ru, two_ru).row(three_ru,
    four_ru).row(five_ru).row(back_ru)
