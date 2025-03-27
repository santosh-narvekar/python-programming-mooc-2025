# WRITE YOUR SOLUTION HERE:
class ListHelper:
  def greatest_frequency(my_list: list):
    numbers_count = {}
    numbers_added = []

    for num in my_list:
      if num not in numbers_added:
        numbers_count[num] = my_list.count(num)
        numbers_added.append(num)
    
    max_frequency_number = 0
    frequency_count = 0

    for num in numbers_count:
      if numbers_count[num] > frequency_count:
        max_frequency_number = num
        frequency_count = numbers_count[num]
    
    return max_frequency_number
  
  def doubles(my_list: list):
    numbers_already_added = []
    numbers_present_atleast_twice = []

    for num in my_list:
      if num not in numbers_already_added:
        numbers_already_added.append(num)
        continue

      if num not in numbers_present_atleast_twice:
        numbers_present_atleast_twice.append(num)
      
    return len(numbers_present_atleast_twice)
  
if __name__ == "__main__":  
  numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
  print(ListHelper.greatest_frequency(numbers))
  print(ListHelper.doubles(numbers))
