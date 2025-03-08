# Making a tic tac to replica using nothing but python 

# we start by setting a global variable to create our Dashboard

import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X" # reprisenting player
#winner = None
game_running = True

# Print Board
def print_gameboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
print_gameboard(board)

# Collect Player input
def PlayerInput(board):
    inp = int(input("Selcet a nomber 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": 
# If the number is within the parameter of 1 - 9 and said slot that the player chose is empty then that is the player position
            board[inp-1] = current_player 
    else: 
        print("Spot's taken !!") 

# checking for win
def checkHorizontal(board):
     global winner 
     if board[0] == board[1] == board[2] and board[1] != "-":
         winner = board[0]
         return True
     elif board[3] == board[4] == board[5] and board[3] != "-":
          winner = board[3]
          return True
     elif board[6] == board[7] == board[8] and board[7] != "-":
          winner = board[6]

          return True
        
def checkVert(board):
     if board[0] == board[3] == board[6] and board[0] != "-":
          winner = board[3]
          return True
     elif board[1] == board[4] == board[7] and board[4] != "-":
          winner = board[4]
          return True
     elif board[2] == board[5] == board[8] and board[5] != "-":
          winner = board[5]
          return True
     
# Switch Player
def player_Turn():
     global current_player 
     if current_player == "X":
          current_player = "O"
     else:
          current_player = "X"

# Check for a tie
def checkTie():
     if "-" not in board: 
          print_gameboard(board)
          print("It is a Tie !!")

# Anounce Winner

def Anounce_W():
     if checkVert(board) or checkHorizontal(board):
          print(f"{winner} is winner")


# Computer (Virtual Oponent)
def computer(board):
     while current_player == "O":
          position = random.randint(0, 8)
          if board[position] == "-":
               board[position] = "O"
               player_Turn()
          
          
# Gameplay 
while game_running: 
   print_gameboard(board)
   PlayerInput(board)
   player_Turn()
   computer(board)
   if checkHorizontal(board) == True:
        print_gameboard(board)
        Anounce_W()
        game_running = False
   if checkVert(board) == True:
        print_gameboard(board)
        Anounce_W()
        game_running = False
   if checkTie() == True:
        checkTie()
        game_running = False
