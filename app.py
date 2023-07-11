from aiogram import executor

from loader import dp, db
import handlers, middlewares
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await db.create()
    await db.create_table_users()
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
