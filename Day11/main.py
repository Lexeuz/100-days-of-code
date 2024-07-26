# Day 11 - Blackjack
import random
from art import logo
import os


def check_deck(deck):
    """Checks if the player has an Ace and a 10 in his deck."""
    if 11 in deck and 10 in deck:
        return True
    else:
        return False


def final_hand(user_cards, pc_cards):
    """Shows the final hand."""
    print(f"    Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
    print(f"    Computer's final hand: {pc_cards}, final score: {sum_cards(pc_cards)}")


def sum_cards(deck):
    total = 0
    for i in deck:
        total += i
    return total


def show_deck(user_cards, pc_cards):
    """Shows the current deck."""
    print(f"    Your cards: {user_cards}, current score: {sum_cards(user_cards)}")
    print(f"    Computer's first card: {pc_cards[0]}")


def blackjack():
    if input("Would you like to play a Game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system("cls")
        print(logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = []
        pc_cards = []

        # Adding initial cards to the decks
        for _ in range(2):
            user_cards.append(random.choice(cards))
            pc_cards.append(random.choice(cards))

        should_continue = True
        while should_continue:
            show_deck(
                user_cards, pc_cards
            )  # Shows the deck of both user player and pc.

            if check_deck(user_cards):
                final_hand(user_cards, pc_cards)
                print(f"You win!")
                should_continue = False
            elif check_deck(pc_cards):
                final_hand(user_cards, pc_cards)
                print(f"Pc got {sum_cards(pc_cards)}, you lose.")
                should_continue = False
            if sum_cards(user_cards) > 21:
                final_hand(user_cards, pc_cards)
                print(f"You went over it, you lose:")
                should_continue = False
            if should_continue:
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    user_cards.append(random.choice(cards))
                else:
                    while sum_cards(pc_cards) <= 21:
                        pc_cards.append(random.choice(cards))
                        if sum_cards(pc_cards) > 21:
                            print("Computer went over it, you win!")
                            final_hand(user_cards, pc_cards)
                            should_continue = False
                        elif sum_cards(pc_cards) == 21:
                            print("Computer's final score is better, you lose!")
                            final_hand(user_cards, pc_cards)
                            should_continue = False
        blackjack()

    else:
        os.system("cls")
        blackjack()


os.system("cls")
blackjack()
