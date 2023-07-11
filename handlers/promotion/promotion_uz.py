from aiogram import types

from loader import dp


@dp.message_handler(text="📣 Aksiyalar/Narxlar")
async def promotion(message: types.Message):
    photo_1 = open("promotion.jpg", "rb")
    photo_2 = open("cost.png", "rb")
    text_1 = "✅ 36 oygacha bo'lib to'lash\n✅ Ortiqcha to'lov 0 %\n✅ Boshlang'ich to'lov 30 % dan\n✅ Talab bo'yicha ipoteka"
    text_2 = "✅ 7 300 000 so'm dan\n✅ 9 100 000 so'm gacha"
    await message.answer_photo(photo_1, caption=text_1)
    await message.answer_photo(photo_2, caption=text_2)
