from translate import Translator
import pyttsx3

engine = pyttsx3.init()

while True:
    text = str(input('Введіть текст: '))
    print('[1] - перекласти з англійської на українську')
    print('[2] - перекласти з української на англійську')
    print('[3] - перекласти з польської на українську')
    print('[4] - перекласти з української на польську')
    what = input('Введіть тип перекладу: ')

    if what == '1':
        translator = Translator(from_lang='en', to_lang='uk')
    if what == '2':
        translator = Translator(from_lang='uk', to_lang='en')
    if what == '3':
        translator = Translator(from_lang='pl', to_lang='uk')
    if what == '4':
        translator = Translator(from_lang='uk', to_lang='pl')


    end_text = translator.translate(text)
    engine.say(end_text)
    engine.runAndWait()
    print()
    print(end_text)

