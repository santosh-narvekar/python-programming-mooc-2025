# Write your solution here
temperature_in_fahrenheit = int(input("Please type in a temperature (F): "))
temperature_in_degree_celsius = ( temperature_in_fahrenheit - 32 ) * 5/9

print(f"{temperature_in_fahrenheit} degrees Fahrenheit equals {temperature_in_degree_celsius} degrees Celsius")

if temperature_in_degree_celsius < 0:
    print("Brr! It's cold in here!")