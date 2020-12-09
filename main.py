import pyttsx3
import datetime
import speech_recognition as sr

"""
sapi5 - SAPI5 on Windows
nsss - NSSpeechSynthesizer on Mac OS X
espeak - eSpeak on every other platform
"""
engine = pyttsx3.init('sapi5')


def speakFunction(audio):
    engine.say(audio)
    engine.runAndWait()


# Introduction function here
def introduction():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speakFunction("Good Morning ")
    elif 12 <= hour < 18:
        speakFunction("Good Afternoon")
    else:
        speakFunction("Good Evening ")
    speakFunction("I am Dp How can I help you")


# Voice recognition function
def get_recognition():
    reCog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        reCog.pause_threshold = 1
        audio = reCog.listen(source)
    try:
        print("Recognition ...")
        input_query = reCog.recognize_google(audio, language='en-nep ')
        print(f'You said: {input_query}\n')
    except Exception as e:
        print("Please try again ")
        return None

    return input_query


def change_voice():
    return 1


def messages():
    while True:
        input_data = get_recognition().lower()
        if "what is your name" in input_data:
            speakFunction("My name is dp ")
            speakFunction("your name please ")
        elif "my name is dp" in input_data:
            speakFunction("nice to meet you")
        elif "do you love me" in input_data:
            speakFunction("Yes I love you")
        elif 'okay' in input_data:
            speakFunction("Thank you ")
        else:
            speakFunction("Sorry I can't understand what you say please tell me again..")


if __name__ == "__main__":
    voice_id = change_voice()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    introduction()
    messages()
