# Write your solution here  

while True:
  editor_choice = input("Editor: ")
  editor_choice = editor_choice.lower()
  if editor_choice == "visual studio code":
    print("an excellent choice!")
    break
  
  if editor_choice == "notepad" or editor_choice == "word":
    print("awful")
  else:
    print("not good")
