# Write your solution here
from datetime import datetime,timedelta

total_minutes = 0
average = 0
minutes_worked_per_date = []
filename = input("Filename: ")
start_date = input("Starting date: ")
how_many_days = int(input("how many days: "))

original_date = datetime.strptime(start_date,"%d.%m.%Y")
start_date = original_date.strftime("%d.%m.%Y") 
end_date = (original_date + timedelta(days = how_many_days - 1) ).strftime("%d.%m.%Y")

print("Please type in screen time in minutes on each day (TV computer mobile):")

for i in range(how_many_days):
  cur_day = original_date + timedelta(days = i)
  formatted_date = cur_day.strftime("%d.%m.%Y")
  og_minutes = input(f"Screen time {formatted_date}: ")
  minutes_for_sum = og_minutes.split(" ")
  minutes_for_storing_data = og_minutes.split(" ")
  index = 0
  
  while index < len(minutes_for_sum):
    minutes_for_sum[index] = int(minutes_for_sum[index])
    index += 1

  total_minutes += sum(minutes_for_sum)
  min_formatted = "/".join(minutes_for_storing_data)

  minutes_worked_per_date.append(f"{formatted_date}: {min_formatted}\n")

average = total_minutes / how_many_days


with open(filename,"w") as new_file:
  new_file.write(f"Time period: {start_date}-{end_date}\n")
  new_file.write(f"Total minutes: {total_minutes}\n")
  new_file.write(f"Average minutes: {average}\n")
  for minutes_per_day in minutes_worked_per_date:
    new_file.write(minutes_per_day)