from aiogram import types

from loader import dp

from states.plans.plans_uz import NewJoyPlan

from keyboards.default_keyboards.quantity_complexes import complexes_uz


@dp.message_handler(text="📋 Uy chizmalari")
async def plans_uz(message: types.Message):
    await message.answer("Blokni tanlang 👇", reply_markup=complexes_uz)
    await NewJoyPlan.quantity_complexes.set()
