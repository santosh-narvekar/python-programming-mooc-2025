# Write your solution here
cur_year = int(input("Year: "))
# 2023 => 2024
next_year = cur_year + 1 

while True:

    if next_year % 4 == 0:
        if next_year % 100 == 0:
            if next_year % 400 == 0:
                break
        else:
            break
    
    next_year += 1

print(f"The next leap year after {cur_year} is {next_year}")
