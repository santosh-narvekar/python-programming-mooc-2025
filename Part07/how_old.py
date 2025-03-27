# Write your solution here
from datetime import datetime
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date_time = datetime(year,month,day)
millenium = datetime(1999,12,31)
no_of_days = millenium - date_time
if millenium >= date_time:
  print(f"You were {no_of_days.days} days old on the eve of the new millennium.")
else:
  print("You weren't born yet on the eve of the new millennium.")