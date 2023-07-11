import re
import aiohttp
import json

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.submit_application.sub_applic import NewJoySubmitApplication
from .first_name_uz import sub_applast_name

from keyboards.default_keyboards.back import back_btn_uz
from keyboards.default_keyboards.sokin_diyor_menu import sokin_diyor_menu_uz


@dp.message_handler(state=NewJoySubmitApplication.phone_number, content_types=types.ContentTypes.ANY)
async def load_contact(message: types.Message, state: FSMContext):
    if message.text == "⬅ Ortga":
        await message.answer("Iltimos ismingizni kiriting 👇", reply_markup=back_btn_uz)
        await NewJoySubmitApplication.first_name.set()
    else:
        if message.content_type == 'text' or message.content_type == 'contact':
            match_number = r'''^(\+998|998)(90|91|99|77|94|93|95|97|98|88|33){1}\d{7}$'''
            phone_number = ""
            if message.contact and re.match(match_number, message.contact.phone_number):
                phone_number = message.contact.phone_number
            elif message.text and re.match(match_number, message.text):
                phone_number = message.text
            else:
                await message.answer(
                    "❌ Telefon raqam xato kiritildi\nRaqamni (+998xxxxxxxxx yoki 998xxxxxxxxx) shaklida yuboring 👇")
                return sub_applast_name
            if phone_number:
                await state.update_data(contact=phone_number)
                datas = await state.get_data()
                fisrt_name = datas.get("first_name")
                contact = datas.get("contact")
                url = "https://newjoy.ikcrm.uz/api/send-data"
                headers = {
                    "Content-Type": "application/json"
                }
                data = {
                    "token": "base64:YXJkX2FwaV90b2tlbl9oYXNo",
                    "telegram": {
                        "first_name": f"{fisrt_name}",
                        "last_name": None,
                        "phone": f"{contact}",
                        "bot_chat_id": 6133260622,
                        "chat_id": int(f"{message.from_user.id}"),
                        "email": None,
                        "username": None,
                        "language": "uz",
                        "address": None,
                        "passport": None,
                        "inn": None,
                        "is_premium": 0
                    }
                }
                json_data = json.dumps(data, indent=4)
                async with aiohttp.ClientSession() as session:
                    await session.post(url, data=json_data, headers=headers, ssl=False)
                await message.answer("✅ Arizangiz uchun rahmat ❗", reply_markup=sokin_diyor_menu_uz)
        await state.finish()
