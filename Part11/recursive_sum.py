# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    # if the number is 1, there is nothing else to add
    
    if number <= 1:   
        return number
    
    return number + recursive_sum(number - 1)

   # fill in the rest of the function

