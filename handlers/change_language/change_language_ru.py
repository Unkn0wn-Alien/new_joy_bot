from aiogram import types

from loader import dp

from states.change_language.change_language_ru import NewJoyChangelanguage

from keyboards.default_keyboards.language import change_lan_ru


@dp.message_handler(text="🌏 Изменить язык")
async def change_lan_to_uz(message: types.Message):
    await message.answer("Выберите язык 👇", reply_markup=change_lan_ru)
    await NewJoyChangelanguage.change_language.set()
