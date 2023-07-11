from aiogram import types

from loader import dp


@dp.message_handler(text="🏢 Proyekt")
async def rendors(message: types.Message):
    photo_1 = open("renders/1.jpg", "rb")
    text_1 = "✅ Toshkent shahar\n✅ Yashnobod tumani\n✅ SGM 'IQBOL' Uysozlar ko'chasi"
    photo_2 = open("renders/2.jpg", "rb")
    text_2 = "✅ Yerosti avtoturargoh"
    photo_3 = open("renders/3.jpg", "rb")
    text_3 = "✅ Bolalar maydonchasi"
    photo_4 = open("renders/4.jpg", "rb")
    text_4 = "✅ Sport maydoni"
    photo_5 = open("renders/5.jpg", "rb")
    text_5 = "✅ Yashil maydondagi qulay besedka"
    photo_6 = open("renders/6.jpg", "rb")
    text_6 = "✅ Qo'riqlanadigan yopiq maydon"
    photo_7 = open("renders/7.jpg", "rb")
    text_7 = "✅ Tijorat maydoni"
    photo_8 = open("renders/8.jpg", "rb")
    text_8 = "✅ Katta transport almashinuvi\n✅ Metrogacha 5 daqiqalik yo'l\n✅ Maktabgacha 100 metr\n✅ Bolalar bog'chasigacha 300 metr"
    await message.answer_photo(photo_1, caption=text_1)
    await message.answer_photo(photo_2, caption=text_2)
    await message.answer_photo(photo_3, caption=text_3)
    await message.answer_photo(photo_4, caption=text_4)
    await message.answer_photo(photo_5, caption=text_5)
    await message.answer_photo(photo_6, caption=text_6)
    await message.answer_photo(photo_7, caption=text_7)
    await message.answer_photo(photo_8, caption=text_8)
