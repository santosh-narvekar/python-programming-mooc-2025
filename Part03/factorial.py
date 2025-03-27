# Write your solution here

while True:
    number = int(input("Please type in a  number: "))

    if number <= 0:
        print("Thanks and bye!")
        break
    
    if number == 1:
        print("The factorial of the number 1 is 1")
    else:
        product = number 
        num = number
        while True: 
            product *= num - 1 
            num -= 1 
            if num == 1:
                break

        print(f"The factorial of the number {number} is {product} ")

