# WRITE YOUR SOLUTION HERE:

class SimpleDate:

  def __init__(self,day,month,year):
    self.day = day
    self.month = month
    self.year = year

  def __str__(self):
    return f"{self.day}.{self.month}.{self.year}"
  
  def __eq__(self,another:"SimpleDate"):
    date1 = f"{self.day}.{self.month}.{self.year}"
    date2 = f"{another.day}.{another.month}.{another.year}"

    return date1 == date2
  
  def __ne__(self,another:"SimpleDate"):
    date1 = f"{self.day}.{self.month}.{self.year}"
    date2 = f"{another.day}.{another.month}.{another.year}"

    return date1 != date2
  
  def __lt__(self,another:"SimpleDate"):
    if self.year < another.year:
      return True
    
    if self.year == another.year:
      if self.month == another.month:
        return self.day < another.day
      else: 
        return self.month < another.month 

    return False
  
  def __gt__(self,another:"SimpleDate"):
    if self.year > another.year:
      return True
    
    if self.year == another.year:
      if self.month == another.month:
        return self.day > another.day
      else: 
        return self.month > another.month 

    return False
  
  def __add__(self,value):
    count = 1
    cur_day = self.day
    cur_month = self.month
    cur_year = self.year

    while count <= value:
      cur_day += 1

      if cur_day > 30:
        cur_day = 1
        cur_month += 1
      
      if cur_month > 12:
        cur_year += 1
        cur_month = 1
        cur_day = 1

      count += 1
    
    return SimpleDate(cur_day,cur_month,cur_year)
  
  def __sub__(self,another: "SimpleDate"):
    start_day = self.day
    start_month = self.month
    start_year = self.year
    end_year = another.year
    end_day = another.day
    end_month = another.month
    day_count = 1
     
    if start_year < another.year:
      end_year = self.year
      end_day = self.day
      end_month = self.month
      start_day = another.day
      start_month = another.month
      start_year = another.year

    if start_year == end_year:
      if start_month == another.month:
        return abs(start_day - another.day)
      month_difference = abs(start_month - another.month)
      day_difference = abs(start_day - another.day)

      return month_difference * 30 - day_difference 
    
    while True:
      start_day -= 1
       
      if start_day < 1:
        start_day = 30
        start_month -= 1
       
      if start_month < 1:
        start_month = 12
        start_day = 30
        start_year -= 1
       
      if start_day == end_day and start_month == end_month and start_year == end_year:
        break

      day_count += 1

    return day_count

