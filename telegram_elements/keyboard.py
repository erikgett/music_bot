from telebot import types


def keyboard():
    agree_kb = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    agree_kb.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    agree_kb.add(key_no)
    question = 'Тестовая клава'
    return question, agree_kb
