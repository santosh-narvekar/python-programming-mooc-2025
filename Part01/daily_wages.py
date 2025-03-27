# Write your solution here

hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
week_day = input("Day of the week: ")
daily_wages = hourly_wage * hours_worked

if week_day == "Sunday":
    daily_wages = daily_wages * 2

print(f"Daily wages: {daily_wages} euros") 