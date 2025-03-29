# Write your solution here
import re

def is_dotw(my_string: str) -> bool:
  if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun",my_string):
    return True
  
  return False

def all_vowels(my_string: str) -> bool:

  for char in my_string:
    if not re.search("a|e|i|o|u",char):
      return False

  return True

def time_of_day(my_string: str) -> bool:
  pattern = "(?:[01]\\d|2[0-3]):[0-5]\\d:[0-5]\\d"

  if re.search(pattern,my_string):
    return True
  
  return False

