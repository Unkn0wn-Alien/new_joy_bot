from aiogram import types

from loader import dp

from states.submit_application.sub_application import NewjoySubmitApplication

from keyboards.default_keyboards.back import back_btn_ru


@dp.message_handler(state="*", text="☎ Связаться с нами")
async def sub_app_first_name(message: types.Message):
    await message.answer("Пожалуйста напишите ваше имя 👇", reply_markup=back_btn_ru)
    await NewjoySubmitApplication.first_name.set()
