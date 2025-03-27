# Write your solution here

def times_ten(start_index: int, end_index: int)->{}:
  times_ten_dict = {}

  for i in range(start_index,end_index + 1):
    times_ten_dict[i] = i * 10

  return times_ten_dict

