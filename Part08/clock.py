# Write your solution here:
class Clock:
  def __init__(self,hours,minutes,seconds):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def tick(self):
     
    if self.seconds >= 59:

      self.minutes += 1

      if self.minutes >= 60:
        self.hours += 1
        self.minutes = 0

      if self.hours >= 24:
        self.hours = 0
        self.minutes = 0

      self.seconds = 0
    
    else:
      self.seconds += 1 

  def set(self,hours,minutes):
    self.hours = hours
    self.minutes = minutes
    self.seconds = 0

  def __str__(self):
    return f"{
      self.hours if self.hours >= 10 else "0"+str(self.hours) 
    }:{
      self.minutes if self.minutes >= 10 else "0"+str(self.minutes)
    }:{
      self.seconds if self.seconds >= 10 else "0"+ str(self.seconds)
    }"
