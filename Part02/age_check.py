# Write your solution here

your_age = int(input("What is your age? "))

if your_age < 0:
    print("That must be a mistake")
elif your_age < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {your_age} years old")