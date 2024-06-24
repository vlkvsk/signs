from .keyboard_imports import *

def main(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='🗂 Каталог сигн', callback_data='dsadsa'))
    keyboard.add(ikb(text='⏳ Заказы', callback_data='profile_menu'), ikb(text='💳 Пополнить баланс', callback_data='sdasdas'))
    keyboard.add(ikb(text='❓ Инфа', callback_data='info_menu'), ikb(text='🆘 Support', callback_data='help_menu'), ikb(text='👑 Профиль', callback_data='profile_menu'))
    if user_id in get_admins():
        keyboard.add(ikb(text='⚡️ Админ меню', callback_data='admin_menu'))
    if user_id in get_models():
        keyboard.add(ikb(text='👱‍♀️ Модель-меню', callback_data='model_menu'))
    return keyboard

def help_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='💻 Саппорт', callback_data='asd'))
    keyboard.add(ikb(text='🔙 Назад', callback_data='back'))
    return keyboard