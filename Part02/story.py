# Write your solution here
story = ""
words_added = ""

while True:

    word = input("Please type in a word: ")
    
    if word == words_added:
        break
    
    words_added = word

    if word == "end":
        break

    story += word + " "

print(story)