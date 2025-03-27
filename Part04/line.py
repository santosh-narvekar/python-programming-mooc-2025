# Write your solution here
# You can test your function by calling it within the following block

def line(no_of_times,text):
    if text == "":
        print("*" * no_of_times)
    else:
        print(text[0] * no_of_times)

if __name__ == "__main__":
    line(5, "x")
    line(7, "%")
    line(10, "LOL")
    line(3, "")