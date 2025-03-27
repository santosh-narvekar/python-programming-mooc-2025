# tee ratkaisu tänne

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_points_file = input("Exam points: ")
course_file = input("Course information: ")

course_name = ""
course_credits = 0

with open(course_file) as new_file:
  course_data = {}
  for line in new_file:
    line = line.strip().split(":")
    course_data[line[0]] = line[1].strip()

  course_name = course_data["name"]
  course_credits = course_data["study credits"] 

students = []

with open(student_file) as new_file:
  for student in new_file:
    student = student.strip().split(";")
    if student[0] == "id": continue
    students.append({
      "id": student[0],
      "name":student[1] + ' ' + student[2]
    })

with open(exercise_file) as new_file:
  for exercises in new_file:
    exercises = exercises.strip().split(";")
    if exercises[0] == "id": continue
  
    for student in students:
      if student["id"] == exercises[0]:
        exercise_points = exercises[1:]
        
        for index in range(len(exercise_points)):
          exercise_points[index] = int(exercise_points[index]) 

        total = sum(exercise_points)
        student["exec_nbr"] = total
        student["exec_pts."] = total // 4

with open(exam_points_file) as new_file:
  for exam_points in new_file:
    exam_points = exam_points.strip().split(";")
    if exam_points[0] == "id": continue
  
    for student in students:
      if student["id"] == exam_points[0]:
        exam_points = exam_points[1:]
        
        for index in range(len(exam_points)):
          exam_points[index] = int(exam_points[index]) 

        total = sum(exam_points)
        student["exm_pts."] = total
        student["tot_pts."] = student["exec_pts."] + student["exm_pts."]

grades = [ [0,14],[15,17],[18,20],[21,23],[24,27],[28,40] ]


for student in students:
  final_grade = 0
  for grade in grades:
    if student["tot_pts."] in range(grade[0],grade[1] + 1):
      student["grade"] = final_grade
      break
    final_grade += 1

with open("results.txt","w") as new_file:
  new_file.write(f"{course_name}, {course_credits} credits\n")
  new_file.write("======================================\n")
  for heading in students[0]:
    if heading == "id": continue
    if heading == "name":
      new_file.write(f"{heading:30}")
    else:
      new_file.write(f"{heading:10}")
  new_file.write("\n")

  for student in students:
    new_file.write(f"{student["name"]:30}{student["exec_nbr"]:<10}{student["exec_pts."]:<10}{student["exm_pts."]:<10}{student["tot_pts."]:<10}{student["grade"]:<10}\n")

with open("results.csv","w") as new_file:
  for student in students:
    new_file.write(f"{student["id"]};{student["name"]};{student["grade"]}\n")

print("Results written to files results.txt and results.csv")