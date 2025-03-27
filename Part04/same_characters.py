# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word,index_1,index_2):
    first_index = 0
    last_index = len(word) - 1

    if index_1 < first_index or index_1 > last_index:
        return False
    
    if index_2 < first_index or index_2 > last_index:
        return False
    
    if word[index_1] == word[index_2]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))