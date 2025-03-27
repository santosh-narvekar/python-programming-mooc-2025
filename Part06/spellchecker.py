# write your solution here
text =  input("Write text: ")

text_input = text.split(" ")
correct_words = []

with open("wordlist.txt") as new_file:
  for word in new_file:
    word = word.strip()
    correct_words.append(word)


for index in range(len(text_input)):
  lower_case_word = text_input[index].lower()
  if lower_case_word not in correct_words:
    text_input[index] = f"*{text_input[index]}*" 


print(" ".join(text_input))
