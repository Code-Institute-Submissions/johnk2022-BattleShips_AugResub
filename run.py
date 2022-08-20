# All credit to YouTuber Knowledge Mavens for most of the code.

# Legend for the maps:
# X shows a hit.
# - shows a miss.
# " " (space) not guessed yet.

# Setup random function
from random import randint

# Setup computer board 8*8 for now
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Setup hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

# Create computer ships x 5


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


# Print Board
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# Convert column letters to numbers
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


# Player Guess
def get_ship_location():
    row = input("Ship Row: ").upper()
    while len(row) == 0:
        row = input("Ship Row: ").upper()
    while row not in "12345678":
        print('Please select a valid row 1 to 8')
        row = input("Ship Row: ").upper()

    column = input("Ship column: ").upper()
    while len(column) == 0:
        column = input("Ship column: ").upper()
    while column not in "ABCDEFGH":
        print('Please select a valid column A to H')
        column = input("Ship column: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# Check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# Main Game
if __name__ == "__main__":
    player1 = input("Enter Your Name : ").upper()
    while len(player1) == 0:
        player1 = input("Enter Your Name : ").upper()
    print ("Hello " + player1 + " !")
    print ("Lets Play Battleships, you have 10 missiles.")
    create_ships(HIDDEN_BOARD)

    turns = 10
    while turns > 0:
        print('Guess a row and column to fire your missile.')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()

        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")

        elif HIDDEN_BOARD[row][column] == "X":
            print(player1 + " HITS!!!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1

        else:
            print(player1 + " MISSES!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1

        if count_hit_ships(GUESS_BOARD) == 5:
            print("Congratulations " + player1 + ", You Win!!!")
            break

        print(player1 + ", you have " + str(turns) + " missiles left")

        if turns == 0:
            print("Sorry " + player1 + ", you ran out of missiles.")
