# write your solution here
def matrix_sum():
  line_numbers = []

  with open("matrix.txt") as new_file:

    for line in new_file:
      line = line.replace("\n","")
      line = line.split(",")
      for num in line:
        line_numbers.append(int(num))

  return sum(line_numbers)
 
def matrix_max():
  line_numbers = []
  with open("matrix.txt") as new_file:

    for line in new_file:
      line = line.replace("\n","")
      line = line.split(",")
      for num in line:
        line_numbers.append(int(num))
  
  return max(line_numbers)

def row_sums():
  line_rows_sum = []
  with open("matrix.txt") as new_file:

    for line in new_file:
      line_row_sum = []
      line = line.replace("\n","")
      line = line.split(",")
      for num in line:
        line_row_sum.append(int(num))
      line_rows_sum.append(sum(line_row_sum))

  return line_rows_sum
