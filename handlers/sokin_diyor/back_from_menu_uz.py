from aiogram import types

from loader import dp

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_uz


@dp.message_handler(text="⬅ Ortga")
async def back_from_menu_uz(message: types.Message):
    await message.answer("Harakatni tanlang 👇", reply_markup=sokin_diyor_uz)
