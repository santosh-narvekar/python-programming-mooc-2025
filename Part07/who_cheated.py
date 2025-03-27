# Write your solution here
from datetime import datetime

def cheaters():
  cheater_students = []
  start_times = []
  
  with open("start_times.csv") as new_file:
    for start_time in new_file:
      start_time = start_time.strip().split(";")
      name = start_time[0]
      hours,minutes = start_time[-1].split(":")
      time  = datetime(2020,1,1,int(hours),int(minutes))
      
      start_times.append({"name":name,"start_time":time})
  
  with open("submissions.csv") as new_file:
    for submission_time in new_file:
      submission_time = submission_time.strip().split(";")
      name = submission_time[0]
      hours,minutes = submission_time[-1].split(":")
      time = datetime(2020,1,1,int(hours),int(minutes))
      for start_time in start_times:
        if start_time["name"] == name and name not in cheater_students:
          no_of_seconds = int(abs((start_time["start_time"] - time).total_seconds()))
          if no_of_seconds > 10800 :
            cheater_students.append(name)
  
  return cheater_students
        

