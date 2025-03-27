# Write your solution here
def length_of_longest(my_list: list) -> int:
  longest_string = my_list[0]

  for string in my_list:
    if len(string) >=len(longest_string):
      longest_string = string

  return len(longest_string)