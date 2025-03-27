# Write your solution here
eating_times_in_week = int(input("How many times a week do you eat at the student cafeteria?"))
student_lunch_price = float(input("The price of a typical student lunch?"))
money_spend_on_groceries = float(input("How much money do you spend on groceries in a week?"))
weekly_food_expenditure = money_spend_on_groceries + (student_lunch_price * eating_times_in_week)
daily_food_expenditure = weekly_food_expenditure / 7

print("Average food expenditure:")
print(f"Daily: {daily_food_expenditure} euros")
print(f"Weekly: {weekly_food_expenditure} euros")
