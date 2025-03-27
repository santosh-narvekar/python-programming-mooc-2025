# Write your solution here
correct_pin = 4321
attempts = 0

while True:
    enter_pin = int(input("PIN: "))
    attempts += 1

    if enter_pin == correct_pin:
        break
    
    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")