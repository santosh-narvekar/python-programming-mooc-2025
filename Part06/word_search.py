# Write your solution here
def find_words(search_term: str):
  words = []
  words_matched = []
  char_indexes = []
  with open("words.txt") as new_file:
    for word in new_file:
      word = word.strip()
      words.append(word)
  
  new_search_term = ""
  
  if "*" in search_term:
    if search_term[0] == "*":
      new_search_term = search_term[1:]
    else:
      new_search_term = search_term[:-1]

  if "." in search_term:
   
    index = 0
    for char in search_term:
      if char != ".":
        char_indexes.append(index)

      index += 1

  for word in words:
      if search_term[0] == "*":
        if word.endswith(new_search_term):
          words_matched.append(word)
      elif search_term[-1] == '*':
        if word.startswith(new_search_term):
          words_matched.append(word)
      elif "." in search_term:
        word_match = True

        if len(search_term) == len(word):
          for index in char_indexes:
            if search_term[index] != word[index]:
              word_match = False
              break
        else:
          word_match = False

        if word_match == True:
          words_matched.append(word)
      else:
        if search_term == word:
          words_matched.append(word)
  return words_matched
