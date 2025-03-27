# Write your solution here

input_string=input("Please type in a string: ")

index = len(input_string) - 1

while index >= 0:
    print(input_string[index:])
    index -= 1
