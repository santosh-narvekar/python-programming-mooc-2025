# Write your solution here
# occurrences cannot overlap => aaaa => a 2nd occurence at 2

word = input("Please type in a string: ")
search_character = input("Please type in a substring: ")
second_occurence = 0
# word => abcabc  methodology aaaa  imitiology im
# search character => ab  o aa 0 4   

search_character_location = word.find(search_character)
start_index = search_character_location + len(search_character) 
first_slice = word[0:start_index]
word_to_be_searched = word[start_index: ]
second_occurence = word_to_be_searched.find(search_character)   

final_position = second_occurence + len(first_slice)

if second_occurence == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {final_position}.")