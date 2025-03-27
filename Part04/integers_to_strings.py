# Write your solution here
def formatted(my_list: list)-> list:
  formatted_list = []

  for number in my_list:
    formatted_list.append(f"{number:.2f}")

  return formatted_list