# Write your solution here
user_dictionary = {}

while True:
  your_choice = int(input("command(1 search, 2 add, 3 quit): "))
 
  if your_choice == 2:
    your_name = input("name: ")
    your_number = input("number: ")
    user_dictionary[your_name] = your_number
    print("ok!")

  if your_choice == 1:
    your_name = input("name: ")
    if your_name in user_dictionary:
       print(user_dictionary[your_name])
    else:
      print("no number")
      
  if your_choice == 3:
    print("quitting...")
    break

