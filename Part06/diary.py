# Write your solution here
while True:
  print("1 - add an entry, 2 - read entries, 0 - quit")

  choice = int(input("Function: "))

  if choice == 1:
    entry = input("Diary entry: ")
    with open("diary.txt","a") as new_file:
      new_file.write(f"{entry}\n")
    print("Diary saved")
  
  if choice == 2:
    print("Entries: ")
    with open("diary.txt") as new_file:
      for entry in new_file:
        entry = entry.strip()
        print(entry)

  if choice == 0:
    print("Bye now!")
    break