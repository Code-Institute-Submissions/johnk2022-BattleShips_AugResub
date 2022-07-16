from random import randint

#Setup computer board 8*8 for now
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
# Setup hits and misses
HITMISS_BOARD = [[" "] * 8 for i in range(8)]

#Create computer ships x 5
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


#Print Board
def print_board(board):
    print("  1 2 3 4 5 6 7 8")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "O".join(row)))
        row_number += 1



#Player Ships
#def get_ship():

#Check if hit / win
#def count_hits():
