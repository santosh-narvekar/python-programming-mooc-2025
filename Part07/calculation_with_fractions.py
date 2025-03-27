# Write your solution here
from fractions  import Fraction

def fractionate(amount: int):
  fraction_list = []
  cur_amount = amount
  
  while cur_amount > 0:
    fraction_list.append(Fraction(1,amount))
    cur_amount -= 1
  
  return fraction_list


