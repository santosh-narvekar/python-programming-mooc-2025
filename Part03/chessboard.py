# Write your solution here

def chessboard(length):
    i = 0
   
    while i < length:
        if i % 2 == 0:
            j = 0
            while j < length:
                if j % 2 == 0:
                    print(1,end="")
                else:
                    print(0,end="")
                j += 1
        else:
            j = 0
            while j < length:
                if j % 2 == 0:
                    print(0,end="")
                else:
                    print(1,end="")
                j += 1
        print()
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
