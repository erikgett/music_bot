from settings import bot
from telegram_elements.keyboard import keyboard_bool
from telegram_elements.messages import hello_message


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, hello_message)
    if '/' not in message.text:
        keyboard_bool(message, 'Как вам данная клавиатура')


bot.polling(none_stop=True, interval=0)
