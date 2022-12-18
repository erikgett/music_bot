from settings import bot
from telegram_elements.keyboard import keyboard_bool, keyboard_menu
from telegram_elements.messages import hello_message, creaters, help_message
from files_analisers.picture_analiser import pick_query
from files_analisers.text_analiser import text_analis
import random
from googletrans import Translator



def send_audio_play_list(text_emotion):
    pass

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if '/start' in message.text:
        bot.send_message(message.from_user.id, hello_message)
        keyboard_menu(message)
    # Здесь у нас идет обработка текстового сообщения пользователя
    else:
        bot.send_message(message.from_user.id, 'Ваше сообщение обрабатывается, вскоре вы получите плейлист)')
        try:
            translator = Translator()
            perevod = translator.translate(message.text, src='ru', dest='en')
            print(perevod.text)
        except Exception as e:
            print(e)
            perevod = 'hi'
        text_emotion = text_analis(perevod)[0][0]['label']

        print(text_emotion)
        bot.send_message(message.from_user.id, text_emotion)

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
    photo_name = str(random.randint(1000, 9999)) + '.jpj'
    with open(photo_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    photo_object_is = pick_query(photo_name)
    what_in_pickture = photo_object_is[0].get('label')
    # ВОТ ТУТ определелено что находится на картиночке и эмоциональная окраска сообщения
    text_emotion = text_analis(what_in_pickture)[0][0]['label']
    print(text_emotion)

bot.polling(none_stop=True, interval=0)
