# Write your solution here
def add_student(students_db:dict,student:str):
  student_info = {"courses_completed":[]}

  if student not in students_db:
    students_db[student] = student_info

def print_student(students_db:dict,student:str):
 
  if student not in students_db:
    print(f"{student}: no such person in the database")
  else:
    
    courses_completed = students_db[student]["courses_completed"]
    courses_done = len(courses_completed)

    print(f"{student}:")
    if courses_done == 0:
      print(' no completed courses')
    else:
      total = 0
      
      print(f" {courses_done} completed courses:")
      for course in courses_completed:
        total += course[1]
        print(f"  {course[0]} {course[1]}")
     
      print(f" average grade {(total / courses_done):.1f}")

def add_course(students_db:dict,student:str,course:tuple):
  student_courses_done = students_db[student]["courses_completed"]
  if course[1] <= 0: return

  for added_course in student_courses_done:
    if added_course[0] == course[0]:
      if added_course[1] < course[1]:
        index = student_courses_done.index(added_course)
        student_courses_done[index] = course
      return 
  
  student_courses_done.append(course)

def summary(students: dict):
  print(f"students {len(students)}")
  student_data = []
  avg_of_students = []

  for student in students:
    total = 0
    length = len(students[student]["courses_completed"])
    for course in students[student]["courses_completed"]:
      total += course[1]
    
    student_data.append((student,length))
    avg_of_students.append((student,total / length))
  
  most_course_completed_student = student_data[0]
  highest_avg_student = student_data[0]

  for student in student_data:
    if student[1] >= most_course_completed_student[1]:
      most_course_completed_student = student
  
  for student in avg_of_students:
    if student[1] >= highest_avg_student[1]:
      highest_avg_student = student
  
  print(f"most courses completed {most_course_completed_student[1]} {most_course_completed_student[0]}")

  print(f"best average grade {highest_avg_student[1]} {highest_avg_student[0]}")

if __name__  == "__main__":
  students = {}
  add_student(students, "Peter")
  add_student(students, "Eliza")
  add_course(students, "Peter", ("Data Structures and Algorithms", 1)) 
  add_course(students, "Peter", ("Introduction to Programming", 1))
  add_course(students, "Peter", ("Advanced Course in Programming", 1))
  add_course(students, "Eliza", ("Introduction to Programming", 5))
  add_course(students, "Eliza", ("Introduction to Computer Science", 4))
  summary(students)