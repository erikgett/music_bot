from googletrans import Translator


def word_trans(word):
    translator = Translator()
    perevod = translator.translate(word, src='ru', dest='en')
    return perevod.text
