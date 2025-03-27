# Write your solution here
def transpose(matrix: list):
 
  copied_matrix = []

  for row in matrix:
    new_row = row[:]
    copied_matrix.append(new_row)

  for row_no in range(len(matrix)):
    for col_no in range(len(matrix)):
      matrix[row_no][col_no] = copied_matrix[col_no][row_no]


if __name__ == "__main__":
  matrix =   [ [ 1, 2, 3 ] , [ 4, 5, 6 ] , [ 7, 8, 9 ]]
  transpose(matrix) 
  print(matrix)