# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(my_string: str)->bool:
  rev_string = ""

  for index in range(len(my_string) - 1,-1,-1):
    rev_string += my_string[index]

  if rev_string == my_string:
    return True
  
  return False

while True:
  string = input("Please type in a palindrome: ")
  check = palindromes(string)
  if check == True:
    print(f"{string} is a palindrome!")
    break

  print("that wasn't a palindrome")