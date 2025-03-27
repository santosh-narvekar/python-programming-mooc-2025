# Copy here code of line function from previous exercise

def line(no_of_times,text):
    if text == "":
        print("*" * no_of_times)
    else:
        print(text[0] * no_of_times)

def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, character)
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(3, "x")