# Write your solution here
def factorials(n: int) -> dict:
  factorial_numbers = {}
  fact = 1
  for i in range(1,n + 1):
    fact *= i  
    factorial_numbers[i] = fact
 
  return factorial_numbers