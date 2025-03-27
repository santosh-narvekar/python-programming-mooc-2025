# Write your solution here
print("Person 1:")
person_1_name = input("Name: ")
person_1_age = int(input("Age: "))
print("Person 2:") 
person_2_name = input("Name: ")
person_2_age =  int(input("Age: "))

if person_1_age > person_2_age:
    print(f"The elder is {person_1_name}")
elif person_2_age > person_1_age:
    print(f"The elder is {person_2_name}")
else:
    print(f"{person_1_name} and {person_2_name} are the same age")