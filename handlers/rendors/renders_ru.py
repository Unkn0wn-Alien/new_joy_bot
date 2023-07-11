from aiogram import types

from loader import dp


@dp.message_handler(text="🏢 Проект")
async def rendors(message: types.Message):
    photo_1 = open("renders/1.jpg", "rb")
    text_1 = "✅ город Ташкент\n✅ Яшнабадский район\n✅ СГМ «Иқбол»  улица  Уйсозлар"
    photo_2 = open("renders/2.jpg", "rb")
    text_2 = "✅ Подземный Паркинг"
    photo_3 = open("renders/3.jpg", "rb")
    text_3 = "✅ Детские Площадки"
    photo_4 = open("renders/4.jpg", "rb")
    text_4 = "✅ Спортивные Площадки"
    photo_5 = open("renders/5.jpg", "rb")
    text_5 = "✅ Уютные Беседки в зеленой зоне"
    photo_6 = open("renders/6.jpg", "rb")
    text_6 = "✅ Охраняемая закрытая территория"
    photo_7 = open("renders/7.jpg", "rb")
    text_7 = "✅ Коммерческие зоны"
    photo_8 = open("renders/8.jpg", "rb")
    text_8 = "✅ Большая Транспортная Развязка\n✅ 5-минут до линии метро\n✅ 100 метров Школа\n✅ 300 метров Детский Садик"
    await message.answer_photo(photo_1, caption=text_1)
    await message.answer_photo(photo_2, caption=text_2)
    await message.answer_photo(photo_3, caption=text_3)
    await message.answer_photo(photo_4, caption=text_4)
    await message.answer_photo(photo_5, caption=text_5)
    await message.answer_photo(photo_6, caption=text_6)
    await message.answer_photo(photo_7, caption=text_7)
    await message.answer_photo(photo_8, caption=text_8)
