from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Kontakt jo'natish", request_contact=True)],
        [KeyboardButton(text="⬅ Ortga")]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

phone_number_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Отправить контакт", request_contact=True)],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True, one_time_keyboard=True
)
