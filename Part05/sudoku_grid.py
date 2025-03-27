# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
  row_numbers = []
  
  for number in sudoku[row_no]:
    if number in row_numbers:
      return False
    
    if number != 0:
      row_numbers.append(number)

  return True

def column_correct(sudoku: list, column_no: int) -> bool:
  numbers_list_for_columns = []

  for row in sudoku:
    number = row[column_no]
   
    if number in numbers_list_for_columns:
      return False
    
    if number != 0:
      numbers_list_for_columns.append(number)

  return True

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
  numbers_in_block = []

  for row_index in range(row_no , row_no + 3):
    for col_index in range(column_no , column_no + 3 ):
      number = sudoku[row_index][col_index]
      if number in numbers_in_block:
        return False
      
      if number != 0:
        numbers_in_block.append(number)
        
  return True

def sudoku_grid_correct(sudoku: list)->bool:
  
  for row_no in range(0,len(sudoku)):
    col_no = row_no
    row_result = row_correct(sudoku,row_no)
    col_result = column_correct(sudoku,col_no)
    if row_result == False or col_result == False:
      return False
  
  # (0,0) (0,3) (0,6)
  # (3,0) (3,3) (3,6)
  # (6,0) (6,3) (6,6)

  for row_no in range(0,len(sudoku),3):
    for col_no in range(0,len(sudoku),3):
      block_result = block_correct(sudoku,row_no,col_no)
      if block_result == False:
        return False
      
  return True
