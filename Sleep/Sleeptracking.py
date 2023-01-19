class SleepTracker():

    def __init__(self) -> None:
        self.start = False

    def goodMorning(self):
        self.start = True

    def goodNight(self):
        self.start = False

        