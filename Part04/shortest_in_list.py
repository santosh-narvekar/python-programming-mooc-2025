# Write your solution here

def shortest(my_list: list) -> str:
  shortest_string = my_list[0]

  for string in my_list[1:]:
    if len(string )  <= len(shortest_string):
      shortest_string = string
    
  return shortest_string
