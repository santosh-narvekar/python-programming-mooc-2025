# write your solution here

student_info = input("Student information: ")
exercises_completed = input("Exercises completed: ")

students_exercise_completed = {}

with open(student_info) as new_file:
  for student in new_file: 
    student = student.strip().split(";")
    if student[0] == "id": continue
    student_id,student_first_name,student_last_name = (student[0],student[1],student[2])
    
    students_exercise_completed[student_id] = [
      student[1] + " " + student[2] 
    ]

with open(exercises_completed) as new_file:
  for exercises_done in new_file: 
    exercises_done = exercises_done.strip().split(";")
    if exercises_done[0] == "id": continue
    student_id,exercises_done_per_day = (exercises_done[0],exercises_done[1:])

    for i in range(len(exercises_done_per_day)):
      exercises_done_per_day[i] = int(exercises_done_per_day[i])
    
    students_exercise_completed[student_id].append(sum(exercises_done_per_day))


for student_id, student_info in students_exercise_completed.items():
  print(student_info[0],student_info[1])