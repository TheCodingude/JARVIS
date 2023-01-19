from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

from Automation.filesManagment import createVsCodeNewProject, createNewWebDevProject, openProject
from Automation.webBrowser import openSite
from Calorie_Tracking.caloriesTracking import CalorieTracker
from Sleep.Alarm import Alarm
from Sleep.Sleeptracking import SleepTracker
from Security.faceRec import faceRecongizer


recongizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 175)


def create_note():
    global recongizer

    speaker.say("What would like to write?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recongizer.listen(mic)

                note = recongizer.recognize_google(audio)
                note = note.lower()

                speaker.say("choose a file name")
                speaker.runAndWait()

                recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recongizer.listen(mic)

                filename = recongizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, "w") as f:
                f.write(note)
                done = True
                speaker.say("note created")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recongizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you, please try again")
            speaker.runAndWait()            
            
            
def add_todo():
    global recongizer

    speaker.say("what would you like to add")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                
                recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recongizer.listen(mic)

                item = recongizer.recognize_google(audio)
                item = item.lower()

                f = open("todos", "a")
                f.write(item)
                f.close()
                done = True
                speaker.say(f"add {item} to your to do list")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recongizer = speech_recognition.Recognizer()
            speaker.say("I did not understand sorry")


def show_todos():

    speaker.say("the items on your to do list are")
    f = open("todos", "r")
    for item in f.readlines():
        speaker.say(item)
    speaker.runAndWait()





def hello():
    speaker.say("hello, what can i do for you?")
    speaker.runAndWait()


def leave():
    speaker.say("Goodbye")
    sys.exit(0)

mappings = {"greeting": hello, "create_note": create_note, "add_todo":add_todo, "show_todos": show_todos, "exit": leave}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:

        try:
            with speech_recognition.Microphone() as mic:

                recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recongizer.listen()

                message: str = recongizer.recognize_google(audio)
                message = message.lower()

            assistant.request(message)
        except speech_recognition.UnknownValueError:
            recongizer = speech_recognition.Recognizer()
