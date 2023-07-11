from aiogram import types

from loader import dp


@dp.message_handler(text="📣 Акции/Цены")
async def promotion(message: types.Message):
    photo_1 = open("promotion.jpg", "rb")
    photo_2 = open("cost.png", "rb")
    text_1 = "✅ Рассрочка до 36 месяцев\n✅ 0% переплат\n✅ От 30% первоначального взноса"
    text_2 = "✅ от 7 300 000 сум\n✅ до 9 100 000 сум"
    await message.answer_photo(photo_1, caption=text_1)
    await message.answer_photo(photo_2, caption=text_2)
