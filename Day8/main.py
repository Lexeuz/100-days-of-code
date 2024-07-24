# # Day 8 - Functions
# def greet_with(name, location):
#     print(f"Your name is {name}")
#     print(f"What is it like in {location}?")

# greet_with(name = "Alexander", location = "Deutschland")

# # Exercise - Paint Area Calculator
# import math
# def paint_calc(height, width, cover):
#     print(f"You'll need {math.ceil((height * width) / cover)} cans of paint.")

# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# # Exercise - Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# n = int(input()) # Check this number
# prime_checker(number=n)

# Exercise - Caesar Cipher
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(plain_text, shift_amount, direction):
    cipher_text = ""
    if direction != "e":
        shift_amount *= -1
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
        else:
            cipher_text += alphabet[alphabet.index(char) + shift_amount]
    print(cipher_text)
    
    
print(logo)

is_on = True
while is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 # Adjusting the number so it fits the range of the list.
    
    caesar_cipher(plain_text=text, shift_amount=shift, direction=direction)
    
    if input("Would you like to continue: Type 'Y' or 'N'. ") != 'Y':
        is_on = False
        print("Goodbye!")