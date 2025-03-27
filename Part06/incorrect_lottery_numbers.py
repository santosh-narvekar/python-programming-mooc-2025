# Write your solution here
def filter_incorrect():
  correct_lottery_numbers = []

  with open("lottery_numbers.csv") as new_file:
    for week_lottery in new_file:
      week_lottery_items = week_lottery.strip().split(";")
      week_day = week_lottery_items[0]
      lottery_numbers = week_lottery_items[1].split(",")
      is_correct = True
   
      try:
        check_num = []
        week_day = week_day.split(" ")[1]
        int(week_day)

        index = 0
        if len(lottery_numbers) >= 7:
          for number in lottery_numbers:
            lottery_numbers[index] = int(number)
            if lottery_numbers[index] < 1 or lottery_numbers[index] > 39:
              is_correct = False
              break
            if lottery_numbers[index] in check_num:
              is_correct = False
              break
            check_num.append(lottery_numbers[index])
            index += 1
        else:
          is_correct = False
      except ValueError:
        is_correct = False
      
      if is_correct:
        correct_lottery_numbers.append(week_lottery)

    with open("correct_numbers.csv","w") as new_file:
      pass

    with open("correct_numbers.csv","w") as new_file:
      for correct_lottery in correct_lottery_numbers:
        new_file.write(correct_lottery)

