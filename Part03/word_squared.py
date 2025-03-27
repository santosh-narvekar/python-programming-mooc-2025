# Write your solution here


def squared(word,length):
    i = 0
    new_word = ""
    count = 0

    while count < (length * length):
        if i > len(word) - 1:
            i = 0
        new_word += word[i]
        i += 1
        count += 1
   
    row_index = 0

    while row_index < length:
        column_index = 0
        while column_index < length:
            print(new_word[column_index],end="")
            column_index += 1
        new_word = new_word[column_index:]
        print()
        row_index += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)

