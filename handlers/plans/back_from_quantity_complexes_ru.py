from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp

from states.plans.plans_ru import NewJoyplan

from keyboards.default_keyboards.sokin_diyor_menu import sokin_diyor_menu_ru


@dp.message_handler(state=NewJoyplan.quantity_complexes, text="⬅ Назад")
async def back_from_quan_comp(message: types.Message, state: FSMContext):
    await message.answer("Выберите действие 👇", reply_markup=sokin_diyor_menu_ru)
    await state.finish()
