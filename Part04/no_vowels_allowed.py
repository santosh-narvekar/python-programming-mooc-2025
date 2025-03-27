# Write your solution here
def no_vowels(string: str):
  vowels = "aeiou"
  new_string = ""
  for char in string:
    if not(char in vowels):
      new_string += char
  
  return new_string

if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))