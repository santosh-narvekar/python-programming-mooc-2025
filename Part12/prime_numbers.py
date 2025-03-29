# Write your solution here
def prime_numbers():
  num = 2

  while True:
    is_prime = True

    for i in range(2,num  - 1):
        if num % i == 0:
           is_prime = False
  
    if is_prime:
       yield num

    num = num + 1
