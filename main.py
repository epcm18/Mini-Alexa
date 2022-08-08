import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 178)

engine.say('Hello, I am Alexa. How can I help you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
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
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('Current time is' + time)
    elif 'are you there' in command:
        talk('Yes, I am here')
    elif 'date' in command:
        date = datetime.datetime.now().date()
        talk(date)
    elif 'are you single' in command:
        talk('No, Im in a relationship with you')
    elif 'how are you' in command:
        talk('im fine, How are you')
    elif 'fine' in command:
        talk('good, How can i help you?')
    elif 'joke' in command or 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'who is' in command or 'what is' in command:
        question = command.replace('who is', ' ')
        question = command.replace('what is', ' ')
        data = wikipedia.summary(question)
        print(data)
        talk(data)
    elif 'thank you' in command:
        talk('you are always welcome')
    elif 'pasindu' in command:
        talk('pasindu is my master. He created me. He is the worlds finest cricketer after virat kohli. What can I do for you?')
    elif 'Im' in command or 'friend' in command:
        talk('Nice to meet you. How can I help you?')
    elif 'create' in command:
        talk('My master is pasindu. He created me. He is the worlds finest cricketer after virat kohli. What can I do for you?')
    else:
        talk('sorry, can you ask me again')


while True:
    run_alexa()


