from assets.data.db import add_user, check_ban, create_tables_if_not_exist, get_user
from assets.keyboard.keyboard_main import main
from .handler_imports import *

@dp.message_handler(commands=('start'), state='*')
async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_name = message.from_user.username
    if check_ban(user_id) == 1:
        return
    await state.finish()

    text = f"""<b>Добро пожаловать в магазин сигн <a href="tg://user?id={user_name}">{message.from_user.full_name}</a></b>"""

    if not user_name:
        await bot.send_message(user_id, "<b>К сожалению, у вас нет username'а Телеграм.\nУстановите его в настройках.</b>")
        return

    if get_user(user_id):
        await bot.send_message(user_id, text, reply_markup=main(user_id))
    else:
        add_user(user_id, user_name)
        await bot.send_message(user_id, text, reply_markup=main(user_id))

@dp.message_handler(commands=['go'], state='*')
async def gogo(message: Message):
    if message.from_user.id in get_admins():
        await create_tables_if_not_exist()
        await bot.send_message(message.from_user.id, "yesss")
    else: pass