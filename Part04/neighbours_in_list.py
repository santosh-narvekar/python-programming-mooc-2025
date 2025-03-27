# Write your solution here
def longest_series_of_neighbours(my_list: list)->int:
  longest_series = 0
  max_longest_series = 0

  for i in range(len(my_list)):
    if i + 1 == len(my_list):
      if abs(my_list[i] - my_list[i - 1]) == 1:
        longest_series += 1
        if longest_series >= max_longest_series:
          max_longest_series = longest_series
      break

    if abs(my_list[i] -my_list[i +  1]) == 1:
      longest_series += 1
    else:
      longest_series += 1
      if longest_series >= max_longest_series:
        max_longest_series = longest_series
      longest_series = 0

  return max_longest_series
  
if __name__ == "__main__":
  my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  print(longest_series_of_neighbours(my_list))

  my_list_1 = [1, 2, 5, 4, 3, 4]
  print(longest_series_of_neighbours(my_list_1))