# Write your solution here
from string import ascii_letters,digits

def change_case(orig_string: str):
  flipped_string = ""

  for char in orig_string:
    if char.islower():
      char = char.upper()
    else:
      char = char.lower()
    flipped_string += char

  return flipped_string

def split_in_half(orig_string: str):
  first_half = orig_string[0: len(orig_string) // 2 ]
  second_half = orig_string[len(orig_string) // 2: ]
  return first_half,second_half

def remove_special_characters(orig_string: str):
  formatted_string = ""

  for char in orig_string:
    if char in ascii_letters or char in digits or char == " ":
      formatted_string += char
  
  return formatted_string

if __name__ == "__main__":
  print(remove_special_characters("This is a test, lets see how it goes!!!11!"))