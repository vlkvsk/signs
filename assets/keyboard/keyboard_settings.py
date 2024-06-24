from .keyboard_imports import *

def admin_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='⛔️ Забанить', callback_data='ban'), ikb(text='🔰 Разбанить', callback_data='unban'))
    keyboard.add(ikb(text='🔍 Искать', callback_data='mailing'), ikb(text='📊 Статистика', callback_data='checkprof'))
    keyboard.add(ikb(text='➕ Создать промо', callback_data='mailing'), ikb(text='💰 Платежки', callback_data='checkprof'))
    keyboard.add(ikb(text='💬 Рассылка', callback_data='mailing'), ikb(text='🔘 Кнопки в рассылке', callback_data='checkprof'))
    keyboard.add(ikb(text='Раздел инфо', callback_data='mailing'), ikb(text='Получить file_id', callback_data='checkprof'))
    keyboard.add(ikb(text='🔙 Назад', callback_data='back'))
    return keyboard

def support_menu():
    keyboard = InlineKeyboardMarkup()
    # keyboard.add(ikb(text='📲 Розсилка', callback_data='mailing'), ikb(text='👨‍💼 Провірити', callback_data='checkprof'))
    keyboard.add(ikb(text='🔙 Назад', callback_data='back'))
    return keyboard

def search_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='👨‍💼 Профиль', callback_data='dsadas'), ikb(text='💡 ID заказа', callback_data='dasdsa'))
    return keyboard

def search_profile_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='➕ Выдать баланс', callback_data='dasdassd'), ikb(text='✏️ Изменить баланс', callback_data='dsad'))
    keyboard.add(ikb(text='✉️ Отправить уведомление', callback_data='dadas'))
    return keyboard