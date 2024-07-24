# # Day 6 - Reborg's code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if wall_on_right() and not wall_in_front():
#         move()
#         if at_goal():
#             break
#     if not wall_on_right():
#         turn_right()
#         move()
#         turn_right()
#         if at_goal():
#             break
#         elif not wall_in_front():
#             move()
#     if wall_in_front():
#         turn_left()

# # Day 7 - Functions
# def my_function():
#     print("Hello")
#     print("Bye")

# my_function()

# Exercise - Hangman
import random            
from art import logo, stages
from word_bank import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed that letter -> {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
  