from .keyboard_imports import *

def back():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='🔙 Назад', callback_data='back'))
    return keyboard

def delete():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(ikb(text='🗑', callback_data='delete_message'))
    return keyboard

# def info_menu():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(ikb(text='', callback_data='dsadsa'))
#     return keyboard