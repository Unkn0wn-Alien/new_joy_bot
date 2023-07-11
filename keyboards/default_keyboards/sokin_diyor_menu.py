from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

leave_applict_uz = KeyboardButton("☎ Biz bilan bog'lanish")
rendor_uz = KeyboardButton("🏢 Proyekt")
plan_uz = KeyboardButton("📋 Uy chizmalari")
promotion_uz = KeyboardButton("📣 Aksiyalar/Narxlar")
back_uz = KeyboardButton("⬅ Ortga")
leave_applict_ru = KeyboardButton("☎ Связаться с нами")
rendor_ru = KeyboardButton("🏢 Проект")
plan_ru = KeyboardButton("📋 Планировки")
promotion_ru = KeyboardButton("📣 Акции/Цены")
back_ru = KeyboardButton("⬅ Назад")
sokin_diyor_menu_uz = ReplyKeyboardMarkup(resize_keyboard=True).row(leave_applict_uz).row(rendor_uz, plan_uz).row(
    promotion_uz).row(back_uz)
sokin_diyor_menu_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(leave_applict_ru).row(rendor_ru, plan_ru).row(
    promotion_ru).row(back_ru)
