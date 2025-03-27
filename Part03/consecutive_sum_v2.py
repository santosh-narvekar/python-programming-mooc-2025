# Write your solution here

limit = int(input("Limit: "))
number = 1
total = 0
template = "The consecutive sum: "

while total < limit:
    total += number
    if total >= limit:
        template += f"{number} = "
    else:
        template += f"{number} + "
    number += 1 
print(template + f"{total}")