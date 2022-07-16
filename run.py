from random import randint

#Setup computer board 8*8 for now
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
# Setup hits and misses
HITMISS_BOARD = [[" "] * 8 for i in range(8)]

#Create computer ships
#def create_ships(board):

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
