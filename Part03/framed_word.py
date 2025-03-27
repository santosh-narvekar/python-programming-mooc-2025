# Write your solution here
word = input("Word: ")
rows = 3
while rows > 0:
    if rows == 2:
        print("*" * 1,end="")
        if len(word) % 2 == 0:
            print(" " * ( (28- len(word)) // 2 ) ,end="")
            print(word,end="")
            print(" " * ( (28 - len(word)) // 2 ) ,end="")
        else:
            print(" " * ( (28- len(word)) // 2 ) ,end="")
            print(word,end="")
            print(" " * ( (28 - len(word)) // 2 + 1 ) ,end="")
        print("*" * 1)
    else:
        print("*" * 30)
    rows -=1 