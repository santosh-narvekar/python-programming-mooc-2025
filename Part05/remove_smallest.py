# Write your solution here
def remove_smallest(numbers: list) -> int:
  smallest_number = min(numbers)

  for number in numbers:
     if number == smallest_number:
        numbers.remove(number)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)