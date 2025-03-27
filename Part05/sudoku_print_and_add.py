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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
  sudoku[row_no][column_no] = number

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

  print_sudoku(sudoku)
  add_number(sudoku, 0, 0, 2)
  add_number(sudoku, 1, 2, 7)
  add_number(sudoku, 5, 7, 3)
  print()
  print("Three numbers added:")
  print()
  print_sudoku(sudoku)