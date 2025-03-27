# Write your solution here
# You can test your function by calling it within the following block

def spruce(size):
    print("a spruce!")

    iterator = 0

    while iterator <= size:
        spaces_to_add  = size - (iterator + 1)
        stars_to_add = iterator * 2

        if iterator == size:
            spaces_to_add = size - 1
            stars_to_add = 0 

        print(" " * spaces_to_add,end="")
        print("*" + ("*" * stars_to_add))
        iterator += 1


if __name__ == "__main__":
    spruce(10)