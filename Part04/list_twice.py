# Write your solution here

original_list = []

while True:
  item = int(input("New item: "))

  if item == 0:
    print("Bye!")
    break 

  original_list.append(item)
  sorted_list = sorted(original_list)
  
  print(f"The list now: {original_list}")
  print(f"The list in order: {sorted_list}")
