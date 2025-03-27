# Write your solution here

def read_input(input_str:str,start_val:int,end_val:int)->int:
  while True:
    try:
      number = int(input(input_str))
      if number <= start_val or number >= end_val:
        print(f"You must type in an integer between {start_val} and {end_val}")
      else:
        return number
    except ValueError:
        print(f"You must type in an integer between {start_val} and {end_val}")
