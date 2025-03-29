from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(course_attempts: list) -> int:
    return reduce(lambda reduced_sum,course:reduced_sum + course.credits,course_attempts,0)

def sum_of_passed_credits(course_attempts: list) -> int:
    return reduce(lambda reduced_sum,course:reduced_sum + course.credits,filter(lambda course: course.grade >= 1 ,course_attempts),0)

def average(course_attempts: list) -> int:
    return reduce(lambda reduced_sum,course:reduced_sum + course.grade,filter(lambda course: course.grade >= 1 ,course_attempts),0) / len(list(filter(lambda course:course.grade >= 1,course_attempts)))

