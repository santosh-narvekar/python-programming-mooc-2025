# write your solution here

student_info_file = input("Student information: ")
exercises_completed_file = input("Exercises completed: ")
exam_points_file = input("Exam points: ")

students_exercise_completed = []

with open(student_info_file) as new_file:
  for student in new_file: 
    student = student.strip().split(";")
    if student[0] == "id": continue
    student_id,student_first_name,student_last_name = (student[0],student[1],student[2])
    
    students_exercise_completed.append({
      "id":student_id,
      "name":student_first_name + " " + student_last_name 
    })

with open(exercises_completed_file) as new_file:
  for exercises_done in new_file: 
    exercises_done = exercises_done.strip().split(";")
    if exercises_done[0] == "id": continue
    student_id,exercises_done_per_day = (exercises_done[0],exercises_done[1:])

    for i in range(len(exercises_done_per_day)):
      exercises_done_per_day[i] = int(exercises_done_per_day[i])

    for student_info in students_exercise_completed:
      if student_info["id"] == student_id:
        student_info["exercise_points"] = sum(exercises_done_per_day)

with open(exam_points_file) as new_file:
  for exam_points in new_file:
    exam_points = exam_points.strip().split(";")
    if exam_points[0] == "id": continue

    student_id,exam_points_per_day = (exam_points[0],exam_points[1:])

    for i in range(len(exam_points_per_day)):
      exam_points_per_day[i] = int(exam_points_per_day[i])

    for student_info in students_exercise_completed:
      if student_info["id"] == student_id:
        student_info["exam_points"] = sum(exam_points_per_day)
        
    
grades = [ [0,14],[15,17],[18,20],[21,23],[24,27],[28,40] ]

for student_info in students_exercise_completed:
  student_info["exercise_points"] = student_info["exercise_points"] // 4
  
  final_grade = 0
  student_total = student_info["exercise_points"] + student_info["exam_points"]
  for grade in grades:
    if student_total in range(grade[0],grade[1] + 1):
      student_info["grade"] = final_grade
      break
    final_grade += 1

  print(student_info["name"],student_info["grade"])