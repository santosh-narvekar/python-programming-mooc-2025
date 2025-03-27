# Write your solution here
from difflib import get_close_matches

text = input("write text: ")
correct_words = []

with open("wordlist.txt") as correct_words_file:
  for word in correct_words_file:
    word = word.strip()
    correct_words.append(word)

text_words = text.split(" ")
incorrect_words = []
for i in range(len(text_words)):
  if text_words[i].lower() not in correct_words:
    incorrect_words.append(text_words[i])
    text_words[i] = f"*{text_words[i]}*"

formatted_text = " ".join(text_words)
print(formatted_text)
print("suggestions:")
for word in incorrect_words:
  string = word + ": " + ", ".join(get_close_matches(word,correct_words))
  print(string)