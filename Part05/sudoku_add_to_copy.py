# Write your solution here

def print_sudoku(sudoku: list):
      for row_no in range(len(sudoku)):
        for col_no in range(len(sudoku)):
          if sudoku[row_no][col_no] != 0:
            print(f"{sudoku[row_no][col_no]} ",end="")
          else:
            print("_ ",end="")
          if col_no == 2 or col_no == 5:
            print(" ",end="")
        print()
        if row_no == 2 or row_no == 5 or row_no == 8:
          print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku_grid = []

  for row_num in range(len(sudoku)):
    if row_num == row_no:
      copied_row = sudoku[row_no][:]
      copied_row[column_no] = number
      sudoku_grid.append(copied_row)
    else:
      sudoku_grid.append(sudoku[row_num])
      
  return sudoku_grid


if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)
