# Write your solution here
from random import shuffle
def words(n: int, beginning: str):
  already_added_words = []
  words_added = []
  with open("Words.txt") as new_file:
    for word in new_file:
      word = word.strip()
      if word not in already_added_words:
        if word.startswith(beginning):
          words_added.append(word)
  
  shuffle(words_added)
  words_filtered = []
  try:
    for i in range(n):
      words_filtered.append(words_added[i])
  except:
    raise ValueError
  return words_filtered

if __name__ == "__main__":
  word_list = words(3, "ca")
  for word in word_list:
    print(word)
