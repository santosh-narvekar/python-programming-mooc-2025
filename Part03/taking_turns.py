# Write your solution here

number = int(input("Please type in a number: "))
i = 1
cur_iteration = 0

while i <= number:
    j = number - cur_iteration
    if i >= j:
        break
    print(i) 
    print(j)
    cur_iteration += 1
    i += 1
    
    
if number % 2 != 0:
    print(i)