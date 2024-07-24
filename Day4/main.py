# Imports
import random
# -----------
# # ----- Exercise - Banker Roulette -----
# names = ["Angela", "Ben", "Jenny", "Chloe", "Alexander"]
# print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")

# # ----- IndexErrors and Working with Nested Lists -----
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
#                "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Appels", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# # ----- Exercise - Treasure Map -----
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?

# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1

# map[letter_index][number_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")

# Exercise - Rock, Paper, Scissors.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options_list = [rock, paper, scissors]

# User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choice = random.randint(0, len(options_list) - 1)
print(f"\nYour choice:\n{options_list[user_choice]}\nPc choice:\n{options_list[pc_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("Invalid input, you lose!")
elif user_choice == pc_choice:
    print("Draw!")
elif user_choice == 2 and pc_choice == 0:
    print("You Lose!")
elif user_choice > pc_choice:
    print("You Win!")
else:
    print("You Lose!")

