class SleepTracker:

    def __init__(self) -> None:
        self.start = False

    def goodMorning(self):
        self.start = False

    def goodNight(self):
        self.start = True

