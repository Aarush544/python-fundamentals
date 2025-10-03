import math
import random

name = input("Enter your name: ")
print(f"Hello {name}")

age = input("Enter your age: ")
print(f"you are {age} years old")

age_next_year = int(age) + 1
print(f"Next year you will be {age_next_year}")

#Challenge 1

color = input("Enter favorite color: ")
print(f"My favorite color is also {color}")

#Challenge 2
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
print(f"The sum of the numbers is {int(num1) + int(num2)}")

#Challenge 3

diameter = int(input("Enter the diameter: "))
radius = diameter/2
print(f"The circle's area is {(radius ** 2) * math.pi}")


# Challenge 4

sides = int(input("Enter how many sides should be in the die: "))
print(f"Result: {random.randint(1, sides)}")
