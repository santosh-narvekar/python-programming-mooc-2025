# tee ratkaisusi tänne
class Course:
  def __init__(self,name,grade,credits):
    self.__name = name
    self.__grade = grade
    self.__credits = credits

  def name(self):
    return self.__name
  
  def grade(self):
    return self.__grade
  
  def credits(self):
    return self.__credits
  
  def __str__(self):
    return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
  
class CourseRecords:
  def __init__(self):
    self.__courses = {}
    
  def add_course(self,name,grade,credits):
    if name in self.__courses:
      if grade > self.__courses[name].grade():
          self.__courses[name] = Course(name,grade,credits)
          return
    else:
      self.__courses[name] = Course(name,grade,credits)
  
  def get_course(self,name):
    if name not in self.__courses:
      return None
    return self.__courses[name]
  
  def statistics(self):
    total_credit = 0
    total_grade = 0

    for course in self.__courses.values():
      total_credit += course.credits()
      total_grade += course.grade()

    mean = round(total_grade / len(self.__courses),1)
    print(f"{len(self.__courses)} completed courses, a total of {total_credit} credits")
    print(f"mean {mean}")
    print("grade distribution")
    
    for cur_grade in range(5,0,-1):
      count = 0

      for course in self.__courses.values():
        if course.grade() == cur_grade:
          count += 1

      print(f"{cur_grade}: {'x' * count}")

class CourseRecordsApplication:
  def __init__(self):
    self.__course_records = CourseRecords()
  
  def help(self):
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")

  def add_new_course(self):
    course_name = input("course: ")
    grade = int(input("grade: "))
    credits = int(input("credits: "))

    self.__course_records.add_course(course_name,grade,credits)

  def get_course_data(self):
    name = input("course: ")
    course_found = self.__course_records.get_course(name)
    if course_found:
      print(course_found)
      return   
    print("no entry for this course")
    
  def get_statistics(self):
    self.__course_records.statistics()

  def execute(self):
    self.help()
    print()
    while True:
      command = int(input("command: "))

      if command == 0:
        break

      if command == 1:
        self.add_new_course()

      if command == 2:
        self.get_course_data()

      if command == 3:
        self.get_statistics()
      
      print()

course_book = CourseRecordsApplication()
course_book.execute()