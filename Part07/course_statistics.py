# Write your solution here
import urllib.request
import json

def retrieve_all():
  my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

  data = json.loads(my_request.read())
  
  courses_active = []

  for course in data:
    if course["enabled"]:
      total = sum(course["exercises"])
      courses_active.append((course["fullName"],course["name"],course["year"],total))
  
  return courses_active

def retrieve_course(course_name: str):
  my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
  data = json.loads(my_request.read())
  weekly_data = {}
  weekly_data["weeks"] = len(data.keys())
  students_no_per_week = []
  hour_total = 0
  exercise_total = 0
  
  for _,week_data in data.items():
    students_no_per_week.append(week_data["students"])
    hour_total += week_data["hour_total"]
    exercise_total += week_data["exercise_total"]
  
  max_students = max(students_no_per_week)
  hours_average = hour_total // max_students
  exercises_average = exercise_total // max_students
  
  weekly_data["students"] = max_students
  weekly_data["hours"] = hour_total
  weekly_data["hours_average"] = hours_average
  weekly_data["exercises"] = exercise_total
  weekly_data["exercises_average"] = exercises_average

  return weekly_data
