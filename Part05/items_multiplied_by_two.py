# Write your solution here
def double_items(numbers: list):
  doubled_items = []

  for number in numbers:
     doubled_items.append(number * 2)

  return doubled_items

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)