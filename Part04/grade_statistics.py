# Write your solution here

def print_statistics(final_points: list,avg:float,pass_percent: float):
  grades_by_points = [
    [0,14],[15,17],[18,20],[21,23],[24,27],[28,30]
  ]

  print("Statistics:")
  print(f"Points average: {avg}")
  print(f"Pass percentage: {pass_percent:.1f}")
  print("Grade distribution:")
  
  for grade in range(len(grades_by_points)-1,-1,-1):
    print(f"{grade}: ",end="")
    for final_point in final_points:
      min_score = grades_by_points[grade][0]
      max_score = grades_by_points[grade][1]
      if final_point in range(min_score , max_score+1):
        print("*",end="")
    print()

def calculate_statistics(exam_points:list,exercises_completed: list):
  exercise_points = []
  final_student_points = []
  average = 0
  passing_percentage = 0
  passed_students = 0

  for exercises_done in exercises_completed:
    exercise_points.append(int(exercises_done/10))

  for i in range(len(exercise_points)):
      total = exam_points[i] + exercise_points[i]
      final_student_points.append(total)

  if len(final_student_points) > 0:
    average = sum(final_student_points) / len(final_student_points)

  for i in range(len(final_student_points)):
    total = exam_points[i] + exercise_points[i]
    if exam_points[i] >= 10 and total > 14:
      passed_students += 1
    else:
      exam_points[i] = 0
      final_student_points[i] = exam_points[i] + exercise_points[i]
 
  if len(final_student_points) > 0:
    passing_percentage = passed_students / len(final_student_points) * 100

  print_statistics(final_student_points,average,passing_percentage)

def main():
  all_exam_points = []
  all_exercises_completed = []

  while True:
    user_input = input("Exam points and exercises completed: ")

    if user_input == "":
      calculate_statistics(all_exam_points,all_exercises_completed)
      break

    exam_point,exercises_completed = user_input.split(" ")

    all_exam_points.append(int(exam_point))
    all_exercises_completed.append(int(exercises_completed))

main()