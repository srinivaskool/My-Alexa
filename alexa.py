import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes
import pywhatkit
import pyautogui as pg
import random
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

first = 0
running = True


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command


def run_alexa():
    global first
    global running
    first = first + 1
    if first == 1:
        talk("I am alexa. Listening to you Srinivas")
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "volume up" in command:
        pg.press("volumeup")
    elif "volume down" in command:
        pg.press("volumedown")
    elif "mute" in command:
        pg.press("volumemute")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
    elif "built" in command:
        talk("I am built by Srinivas")
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "what is" in command:
        thing = command.replace("what is", "")
        t_info = wikipedia.summary(thing, 1)
        print(t_info)
        talk(t_info)
    elif "whatsapp" in command:
        talk("Noted. On it")
        if "whatsapp" in command:
            words = command.split()
            command = " ".join(command.split(" ")[3:-2])
            h_m = words[-1]
            print(h_m)
            h = h_m[0] + h_m[1]
            h = int(h)
            print(h)
            m = h_m[2] + h_m[3]
            m = int(m)
            print(m)
            pywhatkit.sendwhatmsg("+919573550443", command, h, m)
        elif "Dwarak" in command:
            words = command.split()
            command = " ".join(command.split(" ")[3:-2])
            h_m = words[-1]
            print(h_m)
            h = h_m[0] + h_m[1]
            h = int(h)
            print(h)
            m = h_m[2] + h_m[3]
            m = int(m)
            print(m)
            pywhatkit.sendwhatmsg("+919121091825", command, h, m)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "open google" in command:
        webbrowser.open_new("https://google.com")
    elif "open gmail" in command:
        webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
    elif "choose" in command:
        talk("Hmmm. Let me think ")
        words = command.split()
        n = random.randint(0, 1)
        if n == 0:
            talk(words[3])
        else:
            talk(words[-1])
    elif "stop" in command:
        running = False
        talk("Bye Srinivas. I am going to sleep")
    else:
        talk("Please say the command again.")


while running:
    run_alexa()
