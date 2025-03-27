# Write your solution here

sentence = input("Please type in a sentence: ")
index = 0

print(sentence[0])

while index != len(sentence) - 1  :
    if sentence[index] == " ":
        print(sentence[index + 1])
    index += 1