# Control Flow with If / Else and Conditional Operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercise - Odd or Even numbers

number = int(input("Type the number to check: "))

if number % 2 == 0: # Module gives you the reminder of the division.
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Nested if statemens and elif statements
height2 = int(input("What's your hegiht in cm dude? "))

if height2 >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5")
    elif age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Exercise - BMI 2.0
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = weight / height ** 2
print(bmi)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are slightly overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")

# Exercise - Leap Year
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Multiple if statements in Succession
height3 = int(input("What's your hegiht in cm dude? "))

if height3 >= 120:
    print("You can ride the rollercoaster!")
    age2 = int(input("What is your age? "))
    if age2 <= 12:
        total = 5
    elif age2 < 18:
        total = 7
    elif age2 >= 45 and age2 <= 55:
        total = 0
    else:
        total = 12
if input("Do you want photo taken? Y/N: ") == "Y":
    print(f"{f"Please pay ${total + 3}"}")
else:
    print(f"Please pay ${total}")

# Exercise - Pizza Order Practice
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    print(f"Your final bill is: ${bill + 1}")
else:
    print(f"Your final bill is: ${bill}")

# Exercise - Love Calculator
print("The Love Calculator is calculating your score.")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()
c_names = name1 + name2

t = c_names.count("t")
r = c_names.count("r")
u = c_names.count("u")
e = c_names.count("e")

print(f"T occurs {t} times.\nR occurs {r} times.\nU occurs {u} times.\nE occurs {e} times.")
true_sum = t + r + u + e

l = c_names.count("l")
o = c_names.count("o")
v = c_names.count("v")
e = c_names.count("e")

print(f"L occurs {l} times.\nO occurs {o} times.\nU occurs {v} times.\nE occurs {e} times.")
love_sum = l + o + v + e

score = int(str(true_sum) + str(love_sum))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright togethe.")
else:
    print(f"Your score is {score}.")