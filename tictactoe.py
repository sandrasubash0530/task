import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
cplayer = "X"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
   

#take a player 
def playerInput(board):
   inp = int(input("enter a number 1-9 : "))
   if inp >= 1 and inp <= 9 and board[inp-1] == "-":
     board[inp-1] = cplayer
   else:
     print ("Player already in that spot")

     

#check for win or tie
def checkHori(board):
   global winner
   if board[0] == board[1] == board[2] and board[1] != "-":
      winner = board[0]
      return True
   elif board[3] == board[4] == board[5] and board[4] != "-":
      winner = board[3]
      return True
   elif board[6] == board[7] == board[8] and board[7] != "-":
      winner = board[6]
      return True
   

def checkRow(board):
   global winner 
   if board[0] == board[3] == board[6] and board[0] != "-":
      winner = board[0]
      return True
   elif board[1] == board[4] == board[7] and board[1] != "-":
      winner = board[1]
      return True
   elif board[2] == board[5] == board[8] and board[2] != "-":
      winner = board[2]
      return True
   
def checkdia(board):

   global winner 
   if board[0] == board[4] == board[8] and board[4] != "-":
      winner = board[0]
      return True
   elif board[2] == board[4] == board[6] and board[2] != "-":
      winner = board[2]
      return True
   

def checkTie(board):
    global gameRunning
    if "-" not in board :
       printBoard(board)
       print("It Is a Tie ")
       gameRunning = False

def checkWin():
   if checkdia(board) or checkHori(board) or checkRow(board):
      print(f"the winner is {winner}")
      
#switching
 
def switchPlayer():
  global cplayer
  if cplayer == "X":
     cplayer = "O"
  else:
      cplayer = "X"


#computer
def computer(board):
   while cplayer == "O":
      position =  random.randint(0, 8)
      if board[position] == "-":
         board[position] = "O"
         switchPlayer()

while gameRunning:
   printBoard(board)
   playerInput(board) 
   
   switchPlayer()
   computer(board)
   checkWin()
   checkTie(board)
   
