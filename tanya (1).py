import speech_recognition as sr
import pyttsx3
import pywhatkit
from main import reco

import datetime


birth_date = datetime. date(2021, 5, 16)
end_date = datetime.datetime.now().date()
time_difference = end_date - birth_date
age = time_difference. days

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine. setProperty("rate", 200)
engine.runAndWait()

def talk(text):
    engine.say(text)    
    engine.runAndWait()


def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk("hi, how can i help you")
        print('listening...')
        voice = r.listen(source)

        print(voice)

        try:
            command = r.recognize_google(voice)

        except LookupError:
            print("Could not understand audio")

        command = command.lower()
        print(command)
        if 'tanya' in command:
            command = command.replace('tanya', '')
            print(command)
            command = str(command)
            talk(command)


    return command


def run_alexa():
    command = take_command()
    #print(command)
    if 'object detection' or 'detect object' in command:
        talk("opening object detection module")
        reco()
    else:
        talk('Please say the command again.')


while True:
    run_alexa()



r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
    except LookupError:                           # speech is unintelligible
        print("Could not understand audio")