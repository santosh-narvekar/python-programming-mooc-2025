# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds >= 59:
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
            self.seconds = 0
        else:
            self.seconds += 1
        
    def __str__(self):
        return f"{ self.minutes if self.minutes >= 10 else "0"+ str(self.minutes)   }:{self.seconds if self.seconds >= 10 else  "0" +  str(self.seconds) }"
