import os
import random

import pandas as pd

from files_analisers.picture_analiser import pick_query
from files_analisers.text_analiser import text_analis
from settings import bot
from telegram_elements.keyboard import keyboard_menu
from telegram_elements.messages import hello_message, creaters, help_message
from trans import word_trans


def gen_path(name):
    print(os.getcwd())
    pat = os.getcwd() + f'\\music\\{name}.mp3'
    print(pat)
    return pat


def send_audio_play_list(text_emotion):
    print(text_emotion)
    slovaric = {'acousticness': ['caring', 'confusion', 'sadness', 'pride', 'relief'],
                'danceability': ['curiosity', 'amusement', 'surprise'],
                'energy': ['optimism', 'excitement', 'disgust', 'fear', 'anger'],
                'liveness': ['love', 'approval', 'joy', 'neutral', 'realization', 'admiration'],
                'speechiness': ['desire', 'remorse', 'grief', 'annoyance'],
                'valence': ['gratitude', 'disapproval', 'embarrassment', 'nervousness', 'disappointment']}
    pars_value = 'acousticness'

    for key in slovaric:
        t = slovaric[str(key)]
        if text_emotion in str(t):
            pars_value = str(key)

    music = list(pd.read_csv("music.csv").sort_values(pars_value, ascending=False).head(10).name)

    path_music = music

    print(path_music)

    # вернуть пути к файлам музыки
    return music


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if '/start' in message.text:
        bot.send_message(message.from_user.id, hello_message)
        keyboard_menu(message)
    # Здесь у нас идет обработка текстового сообщения пользователя
    else:
        bot.send_message(message.from_user.id, 'Ваше сообщение обрабатывается, вскоре вы получите плейлист)')
        try:
            perevod = word_trans(message.text)
        except:
            perevod = 'hi'
        text_emotion = text_analis(perevod)[0][0]['label']
        playlist = send_audio_play_list(text_emotion)

        # отослать плейлист
        for m in playlist:
            # bot.send_message(message.from_user.id, m)
            try:
                audio = open(gen_path(m), 'rb')
                bot.send_audio(message.from_user.id, audio)
                audio.close()
            except Exception as e:
                print(e)
                pass
        # bot.send_message(message.from_user.id, text_emotion)
        # bot.send_message(message.from_user.id, playlist)


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

    playlist = send_audio_play_list(text_emotion)
    for m in playlist:
        # bot.send_message(message.from_user.id, m)
        try:
            audio = open(gen_path(m), 'rb')
            bot.send_audio(message.from_user.id, audio)
            audio.close()
        except Exception as e:
            print(e)
            pass
    # отослать плейлист


bot.polling(none_stop=True, interval=0)
