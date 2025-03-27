# Write your solution here
def  smallest_average(person1: dict, person2: dict, person3: dict):
 person_list = [person1,person2,person3]
 smallest_average = person1["result1"] + person1["result2"] + person1["result3"]
 smallest_person = person1
 
 for person in person_list:
  avg = person["result1"] + person["result2"] + person["result3"]
  if avg < smallest_average:
   smallest_person = person
   smallest_average = avg

 return smallest_person
