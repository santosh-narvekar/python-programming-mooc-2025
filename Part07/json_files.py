# Write your solution here
import json

def print_persons(filename:str):
  with open(filename) as my_file:
    data = my_file.read()

  all_person_hobbies = json.loads(data)
  
  for person_hobby in all_person_hobbies:
    hobbies = ""
    for single_hobby in person_hobby["hobbies"]:
      hobbies += single_hobby + ", "
    hobbies = hobbies[:-2]
    print(f"{person_hobby["name"]} {person_hobby["age"]} years ({hobbies})")