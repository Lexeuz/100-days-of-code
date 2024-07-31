from game_data import data
from os import system
import random
import art

score = 0

def show_info():
    global score
    print(art.logo)
    print(f"You're right! Current score: {score}")
    
    
def check_answer(user_a, num_a, num_b):
    global score
    if num_a == num_b:
        score += 1
        system('cls')
        show_info()
    elif num_a > num_b and user_a == 'A':
        score += 1
        system('cls')
        show_info()
    elif num_b > num_a and user_a == 'B':
        score += 1
        system('cls')
        show_info()
        return 'Switch'
    else:
        system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return True


def random_data():
    return data[random.randint(0, len(data) - 1)]


def game():
    comp_a = random_data()
    print(art.logo)
    
    should_stop = False
    while not should_stop:

        
        print(f"Compare A: {comp_a["name"]}, a {comp_a["description"]}, from {comp_a["country"]}. Test: {comp_a["follower_count"]}")
        print(art.vs)
        comp_b = random_data()
        if comp_a == comp_b:
            comp_b = random_data()
        print(f"Compare B: {comp_b["name"]}, a {comp_b["description"]}, from {comp_b["country"]}. Test: {comp_b["follower_count"]}")
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        result = check_answer(user_a=answer, num_a=comp_a["follower_count"], num_b=comp_b["follower_count"])
        
        if result == True:
            should_stop = True
        elif result == 'Switch':
            comp_a = comp_b
            
            
system('cls')            
game()
