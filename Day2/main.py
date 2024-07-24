# Data Types
## String--
string = "Hello"[4]
print(string)

## Integer--
integer = 727
print(254 + 543)
# -> Separate long numbers with underscores instead of comas.
print(123_456_789)

# Float--
floating = 3.141559

# Boolean--
boolean1 = True
boolean2 = False

# Type error, Type checking and Type Conversion
num_char = str(len(input("What's your name?\n")))
print(num_char)

# Exercise
number = input("\nType the number: ")
print(int(number[0]) + int(number[1]))

# Mathematical Operations
addition = 3 + 5
subtraction = 7 - 4
multiplication = 3 * 2
division = 6 / 2 # Float
exponent = 2 ** 2

# # PEMDAS - Priorities from the left to the right.
# Parentheses - ()
# Exponents - **
# Multiplication - * | # Division - /
# Addition - + | # Subtraction - -

# Exercise - BMI
height = float(input("What's your height?\n"))
weight = float(input("What's your weight?\n"))

bmi = weight / height ** 2
print(round(bmi, 2)) # After the coma you state how many decimal places you want.

# Number Manipulation
print(4 // 3) # Floor division , use when you want to discard the fractional part.
print(2 / 2) # Normal division, use when you want a more precise result of the division.

# Exercise - Life in weeks
age = int(input("What's your age?\n"))

life_weeks = 52 * (90 - age)
print(f"You have {life_weeks} weeks left.")

# Final Project - Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round(((total_bill * (tip / 100)) + total_bill) / people, 2)}")