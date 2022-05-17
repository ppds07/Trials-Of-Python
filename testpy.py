import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            from soupsieve.util import lower
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
        return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'data' in command:
        talk("sorry i'm not a human")
    elif 'are you single ' in command:
        talk('i am vocie assistance ')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'send a whatsapp message' in command:
        pywhatkit.sendwhatmsg('+9363099128', 'hi', 00, 00)
        print("succesfully send!")

    else:
        talk('please say the command again.')


while True:
    run_alexa()