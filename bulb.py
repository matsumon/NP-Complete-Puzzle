import sys
import time
from random import seed
from random import randint

# generates random numbers
def generateRandom(z):
	seed(1)
	i = 0
	intArray = [[],[]]
	while i<z:
		intArray[0].append(randint(0,m-1))
		intArray[1].append(randint(0,n-1))
		i = i+1
	return intArray
# prints the board in a pretty fashion
def printBoard(gameBoard):
    print("\n")
    holder=[]
    for i in gameBoard:
        temp=[]
        for j in i:
            if(j==-10):
                temp.append("B")
            elif(j==-1000):
                temp.append("L")
            elif(j==0):
                temp.append(" ")
            else:
                temp.append("S")
        print(temp,"\n")
    print("\n")
# checks the board by iterating through the elements in a row and then for a column
#  a more detailed algo walkthrough can be found in the HW6 writeup 
def checkBoard(finalBoard):
    check = True
    tempArray = []
    holder = []
    lightLight = False
    terminal = False
    for row in range(m):
        lightLight = False
        check = True
        tempArray=[]
        for col in range(n):
            if(col == n-1 and finalBoard[row][col] != -1000):
                if(check==True):
                    holder += tempArray
                    if(finalBoard[row][col] != -10):
                        holder.append((row,col))
            elif(finalBoard[row][col]==-10):
                lightLight = False
                if(check==True):
                    holder+=tempArray
                check = True
                tempArray=[]
            elif(finalBoard[row][col] == -1000):
                    check = False
                    if(lightLight==True):
                        terminal = True
                    lightLight = True
                    tempArray=[]
            else:
                if(check==True):
                    tempArray.append((row,col))
            
    holderTwo = []
    lightLight = False
    for col in range(n):
        lightLight = False
        check = True
        tempArray=[]
        for row in range(m):
            if(row == m-1  and finalBoard[row][col] != -1000):
                if(check==True):
                    holderTwo += tempArray
                    if(finalBoard[row][col] != -10):
                        holderTwo.append((row,col))
            elif(finalBoard[row][col]==-10):
                lightLight = False
                if(check==True):
                    holderTwo+=tempArray
                check = True
                tempArray=[]
            elif(finalBoard[row][col] == -1000):
                if(lightLight==True):
                    terminal = True
                lightLight = True
                check = False
                tempArray=[]
            else:
                if(check==True):
                    tempArray.append((row,col))
    duplicates = set(holder).intersection(holderTwo)
    if(len(duplicates) != 0):
        print("Solution doesn't work. Unlit Squares")
    elif(terminal):
        print("Solution doesn't work. Overlapping Lights")
    else:
        print("Solution works")
    printBoard(finalBoard)

# grabbing the user input params
m = int(sys.argv[1])
n = int(sys.argv[2])
board=[]
for i in range(m):
    grid=[]
    for j in range(n):
        grid.append(0)
    board.append(grid)
# randomly generating black squares
blackHole = generateRandom(1)
blackHoleArray= generateRandom(len(blackHole)*2)
length = len(blackHoleArray)
for index in range(len(blackHoleArray[0])-1):
    start=blackHoleArray[0][index]
    end = blackHoleArray[1][index]
    board[start][end] = -10
printBoard(board)
value="start"
# looping until user decides to quit
while(value!="end"):
    value = input("Input 2 space seperated numbers:EX:1 2\nOr end to end the game\n")
    if(value == "end"):
        break
    value = value.split(" ")
    value[0]=int(value[0])
    value[1]=int(value[1])
    if(value[0] > m-1 or value[0] < 0 or value[1] > n-1 or value[1] < 0):
        print("Invalid indices. Please choose between", m-1, " and ", n-1)
    elif(board[value[0]][value[1]]==-10 or board[value[0]][value[1]]==-1000):
        print("Can't print at a black light or at a lightbulb square")
    else:
            board[value[0]][value[1]]=-1000
    printBoard(board)
checkBoard(board)
