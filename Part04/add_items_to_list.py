# Write your solution here
my_list = []
items_to_add = int(input("How many items: "))
cur_item = 1

while cur_item <= items_to_add:
  item = int(input(f"Item {cur_item}: "))
  my_list.append(item)
  cur_item += 1

print(my_list)

