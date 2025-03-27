# write your solution here

def largest():
  largest_num = 0
  with open("numbers.txt") as new_file:
    for num in new_file:
      num = num.replace("\n","")
      if int(num) >= largest_num:
        largest_num = int(num)

  return largest_num
