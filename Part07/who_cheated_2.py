# Write your solution here
from datetime import datetime

def final_points():
  # returns final_points in dictionary format
  # if same submission for same task consider task with hufher points
  # after 3 hours submission dont consider that submission
  student_points = {}
  start_times = []
  submission_times = { }
  
  with open("start_times.csv") as new_file:
    for start_time in new_file:
      start_time = start_time.strip().split(";")
      name = start_time[0]
      hours,minutes = start_time[1].split(":")
      time = datetime(2020,1,1,int(hours),int(minutes))
      start_times.append({"name":name,"start_time":time})

  with open("submissions.csv") as new_file:
    for submission in new_file:
      submission = submission.strip().split(";")
      name = submission[0]
      task_no = int(submission[1])
      points = int(submission[2])
      hours,minutes = submission[-1].split(":")
      end_time = datetime(2020,1,1,int(hours),int(minutes))

      if name not in submission_times:
        submission_times[name]  = [{"end_time":end_time,"task_no":task_no,"points": points}]
      else:
        submission_time_search = submission_times[name]
        submission_time_search.append({ "end_time":end_time,  "task_no": task_no,"points": points  })

  for start_time in start_times:
    name = start_time["name"]
    tasks_with_points = { }
    tot_points = 0

    for data in submission_times[name]:
      if int(abs((start_time["start_time"] - data["end_time"]).total_seconds())) <= 10800:
        if data["task_no"] in tasks_with_points:
          if data["points"] > tasks_with_points[data["task_no"]]["points"]:
            tasks_with_points[data["task_no"]]["points"] = data["points"]
        else:
            tasks_with_points[data["task_no"]] = {
              "points": data["points"]
            }
      
    for _,task_point in tasks_with_points.items():
      tot_points += task_point["points"]
    
    student_points[name] = tot_points
  
  return student_points
    
#final_points()
