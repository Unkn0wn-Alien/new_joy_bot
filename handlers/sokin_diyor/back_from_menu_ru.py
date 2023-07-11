from aiogram import types

from loader import dp

from keyboards.default_keyboards.main_menu_keyboards import sokin_diyor_ru


@dp.message_handler(text="⬅ Назад")
async def back_from_menu_uz(message: types.Message):
    await message.answer("Выберите действие 👇", reply_markup=sokin_diyor_ru)
