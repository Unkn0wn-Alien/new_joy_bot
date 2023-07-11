from aiogram import types

from loader import dp

from states.plans.plans_ru import NewJoyplan

from keyboards.default_keyboards.quantity_complexes import complexes_ru


@dp.message_handler(text="📋 Планировки")
async def plans_uz(message: types.Message):
    await message.answer("Выберите блок 👇", reply_markup=complexes_ru)
    await NewJoyplan.quantity_complexes.set()
