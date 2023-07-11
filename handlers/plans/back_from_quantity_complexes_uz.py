from aiogram import types

from aiogram.dispatcher import FSMContext

from loader import dp

from states.plans.plans_uz import NewJoyPlan

from keyboards.default_keyboards.sokin_diyor_menu import sokin_diyor_menu_uz


@dp.message_handler(state=NewJoyPlan.quantity_complexes, text="⬅ Ortga")
async def back_from_quan_comp(message: types.Message, state: FSMContext):
    await message.answer("Harakatni tanlang 👇", reply_markup=sokin_diyor_menu_uz)
    await state.finish()
