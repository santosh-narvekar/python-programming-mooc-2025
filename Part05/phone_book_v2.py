# Write your solution here
user_dictionary = {}

while True:
  your_choice = int(input("command(1 search, 2 add, 3 quit): "))
 
  if your_choice == 2:
    your_name = input("name: ")
    your_number = input("number: ")
    if your_name in user_dictionary:
      user_dictionary[your_name].append(your_number)
    else:
      user_dictionary[your_name] = [your_number]
    
    print("ok!")

  if your_choice == 1:
    your_name = input("name: ")
    if your_name in user_dictionary:
      for number in user_dictionary[your_name]:
        print(number)
    else:
      print("no number")
   
  if your_choice == 3:
    print("quitting...")
    break


