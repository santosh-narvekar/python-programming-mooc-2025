# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
  numbers_in_block = []

  for row_index in range(row_no , row_no + 3):
    for col_index in range(column_no , column_no + 3 ):
      number = sudoku[row_index][col_index]
      if number in numbers_in_block:
        return False
      
      if number != 0:
        numbers_in_block.append(number)
        
  return True

if __name__ == "__main__":
  sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]

  print(block_correct(sudoku, 0, 0))
  print(block_correct(sudoku, 1, 2))