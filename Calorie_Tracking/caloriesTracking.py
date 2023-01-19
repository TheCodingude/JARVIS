import sqlite3
import speech_recognition


class CalorieTracker:

    def __init__(self, speaker, recongizer) -> None:
        self.db = sqlite3.connect("calories.db")
        self.cursor = self.db.cursor()
        self.speaker = speaker
        self.recongizer = recongizer

    def add_nutrients(self):
        self.done = False
        while not self.done:

            try:
                with speech_recognition.Microphone() as mic:
                    
                    
                    self.recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                    self.speaker.say("How many calories?")
                    self.audio = self.recongizer.listen(mic)

                    calories = int(self.recongizer.recognize_google(self.audio))
                    
                    self.recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                    self.speaker.say("How much sugar?")
                    self.audio = self.recongizer.listen(mic)

                    sugar = int(self.recongizer.recognize_google(self.audio))

                    self.recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                    self.speaker.say("How much fat?")
                    self.audio = self.recongizer.listen(mic)

                    fat = int(self.recongizer.recognize_google(self.audio))

                    self.recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                    self.speaker.say("How much protein?")
                    self.audio = self.recongizer.listen(mic)

                    protein = int(self.recongizer.recognize_google(self.audio))


            except speech_recognition.UnknownValueError:
                self.speaker.say("Sorry, i did not understand")
                self.recongizer = speech_recognition.Recognizer()

