# Write your solution here

user = input("Whom should i sign this to: ")
file_name = input("Where shall i save it: ")

with open(file_name,"w") as new_file:
  new_file.write(f"Hi {user}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

