# Write your solution here
from string import ascii_letters
from string import punctuation

def separate_characters(my_string: str):
  letters_string = ""
  punctuation_string = ""
  remaining_string = ""

  for char in my_string:
    if char in ascii_letters:
      letters_string += char
    elif char in punctuation:
      punctuation_string += char
    else:
      remaining_string += char
  
  return (letters_string,punctuation_string,remaining_string)
