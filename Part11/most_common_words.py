# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):      
  
  words = []
  
  with open(filename) as new_file:
    for line in new_file:
      for word in line.split(" "):
        word = word.strip().replace(".","").replace(",","")
        words.append(word)
  
  words = [word for word in words if words.count(word) >= lower_limit]
  accepted_words = { word: words.count(word) for word in words }
  
  return accepted_words
