# Write your solution here

year = int(input("Please type in a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is a leap year.")
        else:
            print("This year is not a leap year.")
    else:
        print("This year is a leap year.")
else:
    print("This year is not a leap year.")