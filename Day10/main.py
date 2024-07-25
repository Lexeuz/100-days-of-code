# # Day 10 - Functions with Outputs.
# def format_name(f_name, l_name):
#     return f_name.title() + " " + l_name.title()


# print(format_name("aLexander", "eRaSo"))


# # Exercise - Days in Month
# def is_leap(year):
#     """Returns True if the year is Leap and False if is not Leap."""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     """This is a Docstring, is useful to describe the
#     functionalities of a function."""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True and month == 2:
#         return 29
#     else:
#         return month_days[month - 1]


# year = int(input())  # Enter a year
# month = int(input())  # Enter a month
# days = days_in_month(year, month)
# print(days)


# Exercise - Calculator
from art import logo


# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

is_on = True
while is_on:
    num1 = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is the second number?: "))

    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, num3)

    print(f"{first_answer} {operation_symbol} {num3 } = {second_answer}")
