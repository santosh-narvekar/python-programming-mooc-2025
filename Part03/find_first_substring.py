# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

find_char = word.find(char)

word_slice = word[find_char: find_char + 3]

if len(word_slice) > 2:
    print(word_slice)