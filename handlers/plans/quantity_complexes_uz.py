from aiogram import types

from loader import dp

from states.plans.plans_uz import NewJoyPlan


@dp.message_handler(state=NewJoyPlan.quantity_complexes, text=["1-blok", "2-blok", "3-blok", "4-blok", "5-blok"])
async def quan_comp_uz(message: types.Message):
    if message.text == "1-blok":
        complex_1 = open("sokin_diyor_albom_5/Sokin-Diyor-Albom-5_page-0011.jpg", "rb")
        await message.answer_photo(complex_1)
    elif message.text == "2-blok":
        complex_2 = open("sokin_diyor_albom_4/Sokin-Diyor-Albom-4_page-0005.jpg", "rb")
        await message.answer_photo(complex_2)
    elif message.text == "3-blok":
        complex_3 = open("sokin_diyor_albom_2/Sokin-Diyor-Albom-2_page-0005.jpg", "rb")
        await message.answer_photo(complex_3)
    elif message.text == "4-blok":
        complex_4 = open("sokin_diyor_albom_1/Sokin-Diyor-Albom-1_page-0005.jpg", "rb")
        await message.answer_photo(complex_4)
    elif message.text == "5-blok":
        complex_5 = open("sokin_diyor_albom_5/Sokin-Diyor-Albom-5_page-0011.jpg", "rb")
        await message.answer_photo(complex_5)
