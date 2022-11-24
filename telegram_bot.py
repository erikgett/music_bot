import telebot

import settings

bot = telebot.TeleBot(token=settings.token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text:
        bot.send_message(message.from_user.id, "Бот работает")



bot.polling(none_stop=True, interval=0)