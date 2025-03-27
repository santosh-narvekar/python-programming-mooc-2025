# Write your solution here
number = int(input("Please type in a number: "))
first_num = 1

while first_num <= number:
    second_num = 1
    while second_num <= number:
        product = first_num * second_num
        print(f"{first_num} x {second_num} = {product}")
        second_num += 1
    first_num += 1

