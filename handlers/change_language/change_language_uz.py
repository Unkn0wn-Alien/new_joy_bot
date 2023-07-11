from aiogram import types

from loader import dp

from states.change_language.change_language_uz import NewJoyChangeLanguage

from keyboards.default_keyboards.language import change_lan_uz


@dp.message_handler(text="🌏 Tilni o'zgartirish")
async def change_lan_to_ru(message: types.Message):
    await message.answer("Tilni tanlang 👇", reply_markup=change_lan_uz)
    await NewJoyChangeLanguage.change_language.set()
