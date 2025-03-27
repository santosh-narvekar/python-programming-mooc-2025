# Write your solution here


# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.
print("What is the weather forecast for tomorrow?")

temperature_in_degree_celsius = int(input("Temperature: "))
rain_prediction = input("Will it rain(yes/no): ")

"""
Wear jeans and a T-shirt >= 20
I recommend a jumper as well >= 10
Take a jacket with you >= 5
Make it a warm coat, actually >= 0
I think gloves are in order
Don't forget your umbrella!
"""
if temperature_in_degree_celsius > 0:
    print("Wear jeans and a T-shirt")
    if temperature_in_degree_celsius <= 20:
        print("I recommend a jumper as well")
    if temperature_in_degree_celsius <= 10:
        print("Take a jacket with you")
    if temperature_in_degree_celsius <= 5:
        print("Make it a warm coat, actually")
        print("I think gloves are in order")

if rain_prediction == "yes":
    print("Don't forget your umbrella!")
