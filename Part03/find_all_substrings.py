# Write your solution here
# mammoth => m 

word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = 0


while index < len(word):
    if word[index] == char:
        word_slice = word[index:index + 3]
        if len(word_slice) > 2:
            print(word_slice)
    index += 1