# Write your solution here:
from random import randint

def word_generator(characters: str, length: int, amount: int):
  cur = 0
  while cur < amount:
    string_generated = ""
    for _ in range(length):
      string_generated += characters[randint(0,len(characters) - 1)]
    yield string_generated 
    cur += 1

if __name__ == "__main__":
  wordgen = word_generator("abcdefg", 3, 5)
  for word in wordgen:
    print(word)
