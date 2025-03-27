# Write your solution here
# You can test your function by calling it within the following block

def first_word(sentence):
    index = 0
    start_index = 0

    while sentence[start_index] == " ":
        start_index += 1

    index = start_index
    while True:
        if index == len(sentence) - 1:
            index += 1
            break

        if sentence[index] == " ":
            break

        index += 1
     
     
    return sentence[start_index: index]

def second_word(sentence):
    # first check if the string has any spaces
    # if no,return the word , else
    # take the slice from that space
    # take it to the end index or next space
    index = 0
    sentence_contains_spaces = False
    start_index = 0
    while sentence[start_index] == " ":
        start_index += 1
    
    index = start_index
    while index < len(sentence):
        if sentence[index] == " ":
            sentence_contains_spaces = True
            break
        index += 1

    if sentence_contains_spaces == False:
        return sentence
    else:
        sentence = sentence[index + 1: ]
        sentence_index = 0
        sentence_contains_spaces = False
        while sentence_index < len(sentence):
            if sentence[sentence_index] == " ":
                sentence_contains_spaces = True
                break
            sentence_index += 1
        
        if sentence_contains_spaces == False:
            return sentence
        else:
            end_index = sentence_index
            return sentence[0:end_index]

def last_word(sentence):
    index = -1

    while sentence[index] == " ":
        index -= 1

    while sentence[index] != " ":
        index -= 1
        if abs(index) > len(sentence):
            break 

    return sentence[index + 1:] 

if __name__ == "__main__":
    sentence = " it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))