import telebot

import settings
from telegram_elements.keyboard import keyboard

bot = telebot.TeleBot(token=settings.token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text:
        bot.send_message(message.from_user.id, "Бот работает")
    question, keyb = keyboard()
    bot.send_message(message.from_user.id, text=question, reply_markup=keyb)


bot.polling(none_stop=True, interval=0)
