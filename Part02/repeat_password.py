# Write your solution here
password = input("Password: ")

while True:
    confirm_password = input("Repeat password: ")

    if confirm_password == password:
         break
    else:
        print("They do not match!")

print("User account created!")