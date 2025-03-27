# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
  years = []
  dates_got =  sorted(dates)
  for date in dates_got:
    years.append(date.year)

  return years
