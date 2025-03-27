# Write your solution here
from string import ascii_lowercase
from random import shuffle,randint,sample,choice

def generate_strong_password( length: int,have_numbers: bool, have_wildcharacters: bool ) -> str:
    password = []
    for i in range(length):
      index = randint(0,len(ascii_lowercase) - 1)
      password.append(ascii_lowercase[index])

    if have_numbers:
      numbers = [0,1,2,3,4,5,6,7,8,9]

      for i in range(randint(1, len(password) - 1 )):
        password[i] = numbers[randint(0,len(numbers) - 1)]

      shuffle(password)

    if have_wildcharacters:
      wild_characters = ["!","?","=","+","-","(",")","#"]

      lowercase_char_count = 0
      numbers_count = 0
      lowercase_characters_index = []
      numbers_index = []    

      for char_index in range(len(password)):
        if isinstance(password[char_index],int):
          numbers_count += 1
          numbers_index.append(char_index)
        else:
          lowercase_char_count += 1
          lowercase_characters_index.append(char_index)
     
      shuffle(numbers_index)
      shuffle(lowercase_characters_index)

      if lowercase_char_count == 1:
        for i in range(randint(1,len(numbers_index) - 1)):
          password[numbers_index[i]] = wild_characters[randint(0,len(wild_characters) - 1)]
      else:
        for i in range(randint(1,len(lowercase_characters_index) - 1)):
          password[lowercase_characters_index[i]] = wild_characters[randint(0,len(wild_characters) - 1)]
        
    index = 0
    for char in password:
      password[index] = str(char)
      index += 1
    
    return "".join(password)

if __name__ == "__main__":
  for i in range(10):
    print(generate_strong_password(30, True, True))