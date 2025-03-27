# Write your solution here
def distinct_numbers(my_list: list) -> list:
  distinci_numbers_list = []

  for element in my_list:
    if not(element in distinci_numbers_list):
      distinci_numbers_list.append(element)

  return sorted(distinci_numbers_list)