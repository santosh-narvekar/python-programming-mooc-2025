# Write your solution here
def list_sum(list_1: list, list_2: list) -> list:
  new_list = []

  for i in range(0,len(list_1)):
    new_list.append(list_1[i] + list_2[i])

  return new_list

if __name__ == "__main__":
  a = [1, 2, 3]
  b = [7, 8, 9]
  print(list_sum(a, b)) # [8, 10, 12]