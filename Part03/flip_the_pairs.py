# Write your solution here

number = int(input("Please type in a number: "))
i = 1

while i < number:
    i += 1
    if i % 2 == 0:
        print(i)
        print(i - 1)

if number % 2 != 0:
    print(number)