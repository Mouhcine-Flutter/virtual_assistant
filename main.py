import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')


def parler(text):
    engine.say(text)
    engine.runAndWait()


def ecouter():
    try:
        with sr.Microphone() as source:
            print("parlez maintenant")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            command.lower()
    except:
        pass
    return command


def lancer_assistant():
    command = ecouter()
    print(command)
    if 'Bonjour' in command:
        parler("bonjour,comment allez-vous aujourd'hui?")
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parler('il est' + heure)
    elif 'joue une chanson de' in command:
        chanteur = command.replace('joue une chanson de', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    else:
        print('je ne comprends pas')


while True:
    lancer_assistant()
