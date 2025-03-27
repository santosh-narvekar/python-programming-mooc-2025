# Write your solution here
def sum_of_positives(my_list: list) -> int:
  new_list = []

  for item in my_list:
    if item >= 0:
      new_list.append(item)

  return sum(new_list)