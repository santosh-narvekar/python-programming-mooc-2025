# Write your solution here

def row_sums(my_matrix: list):
  for row in my_matrix:
    total_sum = 0
    for num in row:
      total_sum += num
    row.append(total_sum)


