# Write your solution here

def all_the_longest(my_list: list) -> list:
  longest_strings = []
  longest_lengrth = 0

  for string in my_list:
    if len(string) >= longest_lengrth:
      longest_lengrth = len(string)
  
  for string in my_list:
    if len(string) == longest_lengrth:
      longest_strings.append(string)
  
  return longest_strings

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]

  result = all_the_longest(my_list)
  print(result) # ['eleventh']  

  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

  result = all_the_longest(my_list)
  print(result) # ['dorothy', 'richard']