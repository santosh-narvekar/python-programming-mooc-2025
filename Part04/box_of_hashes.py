# Copy here code of line function from previous exercise

def line(no_of_times,text):
    if text == "":
        print("*" * no_of_times)
    else:
        print(text[0] * no_of_times)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
