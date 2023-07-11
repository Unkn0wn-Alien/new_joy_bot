from aiogram import types

from loader import dp

from states.submit_application.sub_applic import NewJoySubmitApplication

from keyboards.default_keyboards.back import back_btn_uz


@dp.message_handler(state="*", text="☎ Biz bilan bog'lanish")
async def sub_app_first_name(message: types.Message):
    await message.answer("Iltimos ismingizni kiriting 👇", reply_markup=back_btn_uz)
    await NewJoySubmitApplication.first_name.set()
