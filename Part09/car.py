# WRITE YOUR SOLUTION HERE:
class Car:
  def __init__(self):
    self.__amount_of_petrol = 0
    self.__odometer_reading = 0
  
  def fill_up(self):
    self.__amount_of_petrol = 60

  def drive(self,km: int):
    if self.__amount_of_petrol > 0:
      if km > self.__amount_of_petrol:
        self.__odometer_reading += self.__amount_of_petrol
        self.__amount_of_petrol = 0
      else:
        self.__odometer_reading += km
        self.__amount_of_petrol -= km   
             
  def __str__(self):
    return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__amount_of_petrol} litres"
