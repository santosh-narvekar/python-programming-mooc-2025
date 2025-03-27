# Write your solution here

while True:
    input_string = input("Please type in a string: ")

    if len(input_string) == 0:
        break

    print(input_string)
    print("-" * len(input_string))