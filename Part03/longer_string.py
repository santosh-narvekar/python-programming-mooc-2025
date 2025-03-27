# Write your solution here
word_1 = input("Please type in string 1: ")
word_2 = input("Please type in string 2: ")
word_1_len = len(word_1)
word_2_len = len(word_2)

if word_1_len < word_2_len:
    print(f"{word_2} is longer")
elif word_2_len < word_1_len:
    print(f"{word_1} is longer")
else:
    print("The strings are equally long")
