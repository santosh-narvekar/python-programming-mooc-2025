# Write your solution here


def anagrams(word_1:str,word_2:str) -> bool:
  word_1 = "".join(sorted(word_1))
  word_2 = "".join(sorted(word_2))
  if word_1 == word_2:
    return True
  return False
  
if __name__ == "__main__":
  print(anagrams("tame", "meta")) # True
  print(anagrams("tame", "mate")) # True 
  print(anagrams("tame", "team")) # True  
  print(anagrams("tabby", "batty")) # False
  print(anagrams("python", "java")) # False