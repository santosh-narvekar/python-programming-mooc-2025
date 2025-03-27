# Write your solution here
def most_common_character(string: str):

  character_count = []
  
  for char in string:
    character_count.append([char,string.count(char)])
  
  max_count = 0
  sorted_character_count = sorted(character_count)
 
  for char_times in sorted_character_count:
    if char_times[1] >= max_count:
      max_count = char_times[1]

  most_occurence_characters = []
  for char_times in sorted_character_count:
    if char_times[1] == max_count:
      most_occurence_characters.append(char_times)

  return most_occurence_characters[0][0]


if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))