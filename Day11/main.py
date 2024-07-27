# Day 11 - Blackjack
import random
from art import logo
import os


def calculate_score(deck):
    """Checks if the player has an Ace and a 10 in his deck or returns the sum of all cards in the deck."""
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    return sum(deck)


def final_hand(user_cards, pc_cards):
    """Shows the final hand."""
    print(
        f"    Your final hand: {user_cards}, final score: {calculate_score(user_cards)}"
    )
    print(
        f"    Computer's final hand: {pc_cards}, final score: {calculate_score(pc_cards)}"
    )


def show_deck(user_cards, pc_cards):
    """Shows the current deck."""
    print(f"    Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
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

            if calculate_score(user_cards) == 0:
                final_hand(user_cards, pc_cards)
                print(f"You win!")
                should_continue = False
            if calculate_score(user_cards) > 21:
                final_hand(user_cards, pc_cards)
                print(f"You went over it, you lose:")
                should_continue = False
            if should_continue:
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    user_cards.append(random.choice(cards))
                else:
                    while calculate_score(pc_cards) <= 21:
                        pc_cards.append(random.choice(cards))
                        if calculate_score(pc_cards) > 21:
                            print("Computer went over it, you win!")
                            final_hand(user_cards, pc_cards)
                            should_continue = False
                        elif calculate_score(pc_cards) == 21:
                            print("Computer's final score is better, you lose!")
                            final_hand(user_cards, pc_cards)
                            should_continue = False
        blackjack()

    else:
        os.system("cls")
        blackjack()


os.system("cls")
blackjack()
