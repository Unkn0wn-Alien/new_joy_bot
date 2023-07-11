from aiogram import types

from loader import dp

from keyboards.default_keyboards.sokin_diyor_menu import sokin_diyor_menu_uz


@dp.message_handler(text="TJM Sokin Diyor")
async def menu_sokin_diyor_uz(message: types.Message):
    await message.answer("Harakatni tanlang 👇", reply_markup=sokin_diyor_menu_uz)
