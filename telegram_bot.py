from settings import bot
from telegram_elements.keyboard import keyboard_bool, keyboard_menu
from telegram_elements.messages import hello_message, creaters, help_message


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if '/start' in message.text:
        bot.send_message(message.from_user.id, hello_message)
        keyboard_menu(message)



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == 'Menu':
        keyboard_menu(call)

    elif 'history' in call.data:
        bot.send_message(call.message.chat.id, 'можно сохранять тут историю запросов/плейлистов')
        keyboard_menu(call)

    elif 'creater' in call.data:
        bot.send_message(call.message.chat.id, creaters)
        keyboard_menu(call)

    elif 'helper' in call.data:
        bot.send_message(call.message.chat.id, help_message)
        keyboard_menu(call)

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.from_user.id, 'Ваше сообщение получено, обработаем в течении минуты')
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    # нужно обработать картинку и выдать плейлист
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)


bot.polling(none_stop=True, interval=0)
