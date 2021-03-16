# IMPORTS


# END OF IMPORTS
# -----------------------------------------
# GLOBAL VARIABLES
# LINE STRING PREDEFINED AND WILL BE REUSED
line = "-----------------------------------------"
player_symbol = 'X'                             # DEFAULT PLAYER SYMBOLE
board = [' ' for x in range(10)]


# END OF GLOBAL VARIABLES
# -----------------------------------------
# GLOBAL FUNCTIONS
def printWelcomeMessage():                      # PRINT A WELCOME MESSAGE
    user_name = input("Enter your name: ")
    print(f"Welcome {user_name} to Tic Tac Toe")
    print(line)


def askPlayerSymbole():                         # ASK PLAYER TO CHOOSE A SYMBOLE
    symbole = input("Please choose your symbole [x/o]: ")
    if symbole == 0 or symbole.lower() == "o":
        return "O"
    else:
        return "X"


def getUserTurn():                              # GET HUMAN PLAYER TURN
    newTurn = input(f"Where to put {[player_symbol]} [1~9]: ")
    return newTurn


def insertLetter(letter, pos):                  # UPDATE THE BOARD WITH THE NEW TURN
    if board[pos] != ' ':                       # CHECK IF THE POSITION IS EMPTRY THEN PUT THE PLAYER TURN THERE
        board[pos] = letter
    else:
        return 'invalid position'


def printBoard(board):                          # PRINT THE BOARD
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('___|___|___')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('___|___|___')
    print(f' {board[7]} | {board[8]} | {board[9]} ')

# END OF GLOBAL FUNCTIONS
# -----------------------------------------
# GLOBALLY CALLED FUNCTIONS


# END OF GLOBALLY CALLED FUNCTIONS
