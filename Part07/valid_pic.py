# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
  string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
  century_marker = ""
  control_character = pic[-1]
  year = 1900

  if len(pic) > 11:
    return False
  
  if "-" in pic:
    century_marker = "-"
  elif "+" in pic:
    century_marker = "+"
    year = 1800
  elif "A" in pic:
    century_marker = "A"
    year = 2000
  else:
    return False
  
  date_of_birth = pic.split(century_marker)[0]
  personal_identifier = pic.split(century_marker)[1][:-1]

  try:
    datetime(year,int(date_of_birth[2:4]),int(date_of_birth[0:2]))
  except:
    return False
  
  control_character_check =  int(date_of_birth + personal_identifier) % 31

  if string[control_character_check] != control_character:
    return False
  
  return True

if __name__ ==  "__main__":
  print(is_it_valid("230827-906F"))
  print(is_it_valid("120488+246L"))
  print(is_it_valid("310823A9877"))
