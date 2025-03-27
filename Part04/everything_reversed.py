# Write your solution here
def everything_reversed(my_list: list) -> list:
  reversed_items_list = []

  for item in my_list[::-1]:
    reversed_items_list.append(item[::-1])
  
  return reversed_items_list

if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)