# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        self.count += 1
        self.numbers += number

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.numbers == 0:
            return 0
        else:
            return self.numbers / self.count
        

stats = NumberStats()
print("Please type in integer numbers:")
even_numbers_sum = NumberStats()
odd_numbers_sum = NumberStats()

while True:
    num = int(input())

    if num == -1:
        break

    if num % 2 == 0:
        even_numbers_sum.add_number(num)
    else:
        odd_numbers_sum.add_number(num)

    stats.add_number(num)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even_numbers_sum.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers_sum.get_sum()}")

