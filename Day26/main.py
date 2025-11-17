# Frank Alexander Eraso Adarme - 17.11.2025
# Text-based Slot Machine Game in Python: Simulates a virtual slot machine where users can deposit money,
# choose bet lines and amounts, spin the reels, and win or lose based on matching symbols.
# Implements core Python concepts including loops, lists, dictionaries, functions, input validation,
# and randomization, providing a complete, interactive game experience.

# <------------- LIBRARIES ------------------>
import random


# <-------------- CONSTANTS ------------------->
MAX_LINES = 3 # Constant value.
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Defining values of the symbols that will pop-up on the wheel.
symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}



# <----------------------- FUNCTIONS -------------------------->
symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


# <----------------------- FUNCTIONS -------------------------->
def check_winnings(columns, lines, bet, values):
    # ---------------------------------------------------------
    # Purpose:
    # Check which lines (rows) of the slot machine contain the
    # same symbol across all columns -> this means the player won.
    #
    # Parameters:
    # columns -> list of columns; e.g.:
    #       [
    #         ['A','B','C'],   # column 1
    #         ['A','C','C'],   # column 2
    #         ['A','B','C']    # column 3
    #       ]
    #
    # lines -> number of horizontal lines the player is betting on
    # bet -> how much money the player bet per line
    # values -> dictionary linking symbols to their payout values
    #           {'A':5, 'B':4, 'C':3, 'D':2}
    # ---------------------------------------------------------

    winnings = 0  # Total winnings calculated per winning line.
    winning_lines = []  # Store which lines won (line numbers).

    # Loop through each line the user is betting on.
    for line in range(lines):

        # Take the symbol in the first column for this line.
        # Example: columns[0][line] = symbol in column 1, row 'line'
        symbol = columns[0][line]

        # Check if this symbol matches in every column for this line.
        for column in columns:
            symbol_to_check = column[line]  # Symbol in current column in same row.

            # If ANY column has a different symbol → this line is NOT a winning line.
            if symbol != symbol_to_check:
                break

        else:
            # The 'else' here connects to the 'for' loop above.
            # It runs ONLY if the for-loop didn't break, meaning:
            #     all symbols matched in all columns.
            
            # Add payout: symbol value × bet amount
            winnings += values[symbol] * bet

            # Save winning line number (1-indexed for UI clarity)
            winning_lines.append(line + 1)
    
    # Return the total winnings and which lines won
    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    # ------------------------------------------
    # Step 1: Build the symbol pool (all_symbols)
    # ------------------------------------------
    # This list will contain each symbol repeated according to its frequency.
    # Example: {'A': 2, 'B': 3} -> ['A', 'A', 'B', 'B', 'B']
    all_symbols = []  # Empty list to store all generated symbols.

    # Loop through each key-value pair in the dictionary.
    # symbols.items() returns pairs like ('A', 2), ('B', 4)
    # 'symbol' receives the key, and 'symbol_count' receives the value.
    for symbol, symbol_count in symbols.items():
        # Add the symbol to all_symbols as many times as its count.
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            # After the full loop, all_symbols becomes a weighted pool
            # that represents the probability distribution.


    # ---------------------------------------------------------
    # Step 2: Generate all slot machine columns (reels of icons)
    # ---------------------------------------------------------
    columns = []  # Final structure: list of columns, each column is a list of symbols.

    # Create 'cols' number of columns (e.g., 3 columns for a 3x3 slot).
    for col in range(cols):
        column = []  # One empty column.
        
        # Make a copy of all_symbols so each column draws from the same pool.
        # Using [:] ensures a *separate* list, avoiding modifications of original data.
        current_symbols = all_symbols[:]  

        # Fill each column with 'rows' symbols (e.g., 3 rows for a 3x3 grid).
        for _ in range(rows):
            # Randomly select a symbol from the weighted pool.
            value = random.choice(current_symbols)

            # Remove it so it cannot be selected again inside the same column.
            # This simulates "no duplicate symbol usage per column" beyond available count.
            current_symbols.remove(value)

            # Add the chosen symbol to the current column.
            column.append(value)

        # When the column is fully built, store it.
        columns.append(column)

    # columns now looks like:
    # [
    #   ['A', 'B', 'C'],   # column 1
    #   ['C', 'A', 'B'],   # column 2
    #   ['B', 'C', 'A']    # column 3
    # ]
    return columns


def print_slot_machine(columns):
    # --------------------------------------------------------
    # This function prints the slot machine row by row, not by
    # column, because humans visually read slots horizontally.
    #
    # Example structure of 'columns':
    # [
    #   ['A','B','C'],   # column 1
    #   ['C','A','B'],   # column 2
    #   ['B','C','A']    # column 3
    # ]
    #
    # Output printed looks like:
    # A | C | B
    # B | A | C
    # C | B | A
    # --------------------------------------------------------

    # Loop through each row index based on the first column's length.
    for row in range(len(columns[0])):

        # Now go column by column and print the symbol in the same row index.
        for i, column in enumerate(columns):

            # If it's NOT the last column → print symbol + "|"
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                # Last column → print only the symbol (end of row)
                print(column[row], end="")
        
        print() # New line.


def deposit():
    # Function Purpose:
    # -----------------
    # Ask the user how much money they want to deposit.
    # Ensure the input is a valid positive integer.
    # Return the deposit amount once validated.

    while True:  # Loop until the user enters a correct value.
        amount = input("What would you like to deposit? $")  
        # Input comes as a STRING. Example: "50"

        if amount.isdigit():  
            # isdigit() checks if every character is numeric AND positive (no negative signs, no decimals)

            amount = int(amount)  # Now it's safe to convert to int.

            if amount > 0:  # Must be a positive number
                break  
            else:
                print("Amount must be greater than 0.")
        else:
            # Input contains something that is not digits:
            # letters, symbols, decimals, negatives, spaces → all invalid
            print("Please enter a number.")

    return amount  # Validated deposit amount as an integer


def get_number_of_lines():
    # Function Purpose:
    # -----------------
    # Ask the user how many lines they want to bet on.
    # Only values between 1 and MAX_LINES (a constant defined elsewhere) are allowed.

    while True:  # Keep asking until a correct input is given.
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit(): 
            # Prevent crashing from converting invalid text into int.
            lines = int(lines)

            # Check if input is between allowed limits.
            # Python allows this nice chained comparison:
            #   1 <= lines <= MAX_LINES
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines  # Validated number of lines



def get_bet():
    while True:
        # Ask the user how much they want to bet per line.
        amount = input("What would you like to bet on each line? $")

        # Check if the input contains only digits (no letters, symbols, spaces, etc.)
        if amount.isdigit():
            amount = int(amount)  # Convert the string to an integer.

            # Validate that the bet amount is within allowed limits (MIN_BET to MAX_BET).
            # Example: MIN_BET = 1 and MAX_BET = 100
            if MIN_BET <= amount <= MAX_BET:
                break  # Valid input, exit the loop.
            else:
                # If the value is outside the allowed range, notify the user.
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            # If the user writes something that's not a number.
            print("Please enter a number.")

    return amount  # Return the valid bet amount.


# <---------------- MAIN CODE ----------------------->

def spin(balance):
    # Ask the user how many lines they want to bet on.
    lines = get_number_of_lines()

    # Make sure the user has enough balance to cover the total bet.
    while True:
        bet = get_bet()                 # How much they want to bet per line.
        total_bet = bet * lines         # Total bet = amount per line × number of lines.

        # Check if the user has enough money.
        if total_bet > balance:
            print(f"Sorry, your betting amount is higher than your deposit's amount. Your current balance is ${balance}")
        else:
            break  # Sufficient balance → exit the loop.

    # Inform the user what their bet is.
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    # Generate the slot machine result (columns with random symbols).
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    # Display the slot machine on screen.
    print_slot_machine(slots)

    # Check if the player won anything.
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    # Show winnings.
    print(f"You won ${winnings}.")
    print(f"You won on", *winning_lines)

    # Return net result: winnings minus the total amount spent (bet).
    return winnings - total_bet



def main():  # Program start (entry point of the game).
    balance = deposit()  # Ask the user to deposit money before playing.

    # Main game loop — keeps running until user quits.
    while True:
        print(f"Current balance is: ${balance}")

        # If user presses Enter → play. If they type "q" → quit.
        answer = input("Press enter to play. (q to quit)")
        if answer == "q":
            break

        # Adjust balance based on winnings or losses.
        balance += spin(balance)

    # Game ended → show final balance.
    print(f"You left with ${balance}")


# Start the entire program.
main()


