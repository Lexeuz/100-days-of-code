# Day 5
# # For Loops and Python Lists
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit + " Pie")

# # Exercise - Average Height
# student_heights = [156, 178, 165, 171, 187]

# sum_height = 0
# total_students = 0
# for height in student_heights:
#     sum_height += height
#     total_students += 1

# print(f"Total height: {sum_height}")
# print(f"Number of students: {total_students}")
# print(f"Average height: {round(sum_height / total_students)}")

# # Exercise - High Score
# high_score = 0
# student_scores = [78, 65, 89, 55, 91, 64, 89]
# for score in student_scores:
#     if score > high_score:
#         high_score = score

# print(f"The highest score is: {high_score}")

# # For Loops and range() function
# total = 0
# for x in range(0, 101, 3):
#     total += x
# print(total)

# # Exercise - Adding Even Numbers
# totalv2 = 0
# for number in range(0, 101, 2):
#     totalv2 += number

# print(totalv2)

# # Exercise - FizzBuzz
# for num in range(0, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# Exercise - Password Generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for _ in range(0, nr_letters):
    password += random.choice(letters)
for _ in range(0, nr_symbols):
    password += random.choice(symbols)
for _ in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_char = list(password)
random.shuffle(list_char)
print(''.join(list_char))
