# Write your solution here

def row_correct(sudoku: list, row_no: int):
  row_numbers = []
  
  for number in sudoku[row_no]:
    if number in row_numbers:
      return False
    
    if number != 0:
      row_numbers.append(number)

  return True


