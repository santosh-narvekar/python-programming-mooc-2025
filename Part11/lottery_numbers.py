# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
  def __init__(self,week_no:int,integers: list):
    self.__week_no = week_no
    self.__integers = integers

  def number_of_hits(self,numbers: list):
    return len([number for number in numbers if number in self.__integers])
  
  def hits_in_place(self,numbers: list):
    return [ number if number in self.__integers else -1 for number in numbers ]
