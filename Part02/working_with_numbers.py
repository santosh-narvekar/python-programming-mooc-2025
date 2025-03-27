# Write your solution here

numbers_count = 0
numbers_sum = 0
positive_numbers = 0
negative_numbers  = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    numbers_count += 1
    numbers_sum += number
    
    if number < 0:
        negative_numbers += 1
    else:
        positive_numbers += 1

numbers_mean = numbers_sum / numbers_count
"""
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5
Positive numbers 3
Negative numbers 1
"""
print("... the program asks for numbers")
print(f"Numbers typed in {numbers_count}")
print(f"The sum of the numbers is {numbers_sum}")
print(f"The mean of the numbers is {numbers_mean}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")
    
    