# Write your solution here
name = input("Please tell me your name: ")
price = 5.90
if name != "Jerry":
    soup_portions = int(input("How many portions of soup? "))
    total_cost = soup_portions * price
    print(f"The total cost is {total_cost}")

print("Next please!")