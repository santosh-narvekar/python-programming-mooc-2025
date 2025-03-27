# Write your solution here

while True:
  print("1 - Add word, 2 - Search, 3 - Quit")
  choice = int(input("Function: "))
  
  if choice == 1:
    finnish_word = input("The word in Finnish: ")
    english_word = input("The word in English: ")
    with open("dictionary.txt","a") as new_file:
      new_file.write(f"{finnish_word}:{english_word}\n")
    print("Dictionary entry added")

  if choice == 2:
    search_term = input("Search term: ")
    with open("dictionary.txt") as new_file:
      for meaning in new_file:
        meaning = meaning.strip().split(":")
        if search_term in meaning[0] or search_term in meaning[1]:
          print(f"{meaning[0]} - {meaning[1]}")
  
  if choice == 3:
    print("Bye!")
    break

