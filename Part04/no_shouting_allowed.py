# Write your solution here

def no_shouting(my_list: list) -> list:
  no_uppercase_list = []

  for string in my_list:
    if not(string.isupper()):
      no_uppercase_list.append(string)

  return no_uppercase_list

if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)