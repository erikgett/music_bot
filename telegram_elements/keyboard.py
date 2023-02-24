from telebot import types
from settings import bot


# вызов данной клавиатуры это да и нет с вашим вопросом
def keyboard_bool(message, question):
    '''

    :param message:
    :param question:
    :return:
    '''
    agree_kb = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    agree_kb.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    agree_kb.add(key_no)
    bot.send_message(message.from_user.id, text=question, reply_markup=agree_kb)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":
            bot.send_message(call.message.chat.id, 'ДААА')
        elif call.data == "no":
            bot.send_message(call.message.chat.id, 'Неет')


def keyboard_menu(mesg):
    menu_btms = types.InlineKeyboardMarkup()
    samples = types.InlineKeyboardButton(text='История', callback_data='history')
    scripts = types.InlineKeyboardButton(text='О создателях', callback_data='creater')
    help = types.InlineKeyboardButton(text='Помощь', callback_data='helper')
    menu_btms.add(samples, scripts, help)
    try:
        bot.send_message(mesg.message.chat.id, text='Ждем ваше письмо!:', reply_markup=menu_btms)
    except:
        bot.send_message(mesg.from_user.id, text='Ждем ваше письмо!:', reply_markup=menu_btms)
