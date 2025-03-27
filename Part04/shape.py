# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(no_of_times,text):
    if text == "":
        print("*" * no_of_times)
    else:
        print(text[0] * no_of_times)

def shape(tri_size_rec_widtg,triangle_char,rec_height,rectangle_char):
    triangle_row = 1
    while triangle_row <= tri_size_rec_widtg:
        line(triangle_row,triangle_char)
        triangle_row += 1

    rectangle_row = 1 
    while rectangle_row <= rec_height:
        line(tri_size_rec_widtg,rectangle_char)
        rectangle_row += 1
        
if __name__ == "__main__":
    shape(5, "x", 2, "o")