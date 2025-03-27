# Write your solution here
input_string = input("Please type in a string: ")
second_char = input_string[1]
second_to_last_char = input_string[-2]

if second_char == second_to_last_char:
    print(f"The second and the second to last characters are {second_char}")
else:
    print("The second and the second to last characters are different")