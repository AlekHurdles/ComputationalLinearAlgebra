import numpy as np
import math as math

class Line:
        # Start Row
        def get_startRow(self):
            return self.startRow

        def set_startRow(self, row):
            self.startRow = row

        # Start Column
        def get_startCol(self):
            return self.startCol

        def set_startCol(self, col):
            self.startCol = col

        # End Row
        def get_endRow(self):
            return self.endRow

        def set_endRow(self, row):
            self.endRow = row

        # End Column
        def get_endCol(self):
            return self.endCol

        def set_endCol(self, col):
            self.endCol = col

        # Calculate Midpoint of line
        def set_midpointRow(self, startRow, endRow):
            # Add the rows and divide by 2
            self.midpointRow = (startRow + endRow) / 2

        def get_midpointRow(self):
            return self.midpointRow

        def set_midpointCol(self, startCol, endCol):
            # Add Columns from the 2 points and divide by 2
            self.midpointCol = (startCol + endCol) / 2

        def get_midpointCol(self):
            return self.midpointCol


def validateMidpoint(kValue,i):
    #Check for matching midpoints in past k turns

    currentObject = objectList[i]
    currentIndex = i
    kValIndexs = i - kValue
    initKList = objectList[0:kValue]
    kList = objectList[kValIndexs:i]
    validMidpoint = True

    if (0 < i < kValue):
        for Line in range(currentIndex):

            if (initKList[Line].midpointRow == currentObject.midpointRow and initKList[Line].midpointCol == currentObject.midpointCol):
                validMidpoint = False
                print("INVALID Midpoint")


    if (len(kList) > 0):
        for Line in range(len(kList)):
            if (kList[Line].midpointRow == currentObject.midpointRow and kList[Line].midpointCol == currentObject.midpointCol):
                validMidpoint = False
                print("INVALID Midpoint")

    return validMidpoint


def validateCells(kValue, i):
    # Start and End cells must be empty
    # The cell is not empty if it has been played as the start or end cell in the past K turns
    currentObject = objectList[i]
    currentIndex = i
    kValIndexs = i - kValue
    initKList = objectList[0:kValue]
    kList = objectList[kValIndexs:i]
    validCells = True

    if (0 < i < kValue):
        for Line in range(currentIndex):

            # Check that the start cell == start cell
            if int(initKList[Line].startRow) == int(currentObject.startRow) and int(initKList[Line].startCol) == int(currentObject.startCol):
                validCells = False
                print("INVALID Starting Cell")

            # Check if the start cell == end cell
            elif int(currentObject.endRow) == int(initKList[Line].startRow) and int(currentObject.endCol) == int(initKList[Line].startCol):
                validCells = False
                print("INVALID End Cell")

            # Check if end cell == end cell
            elif int(initKList[Line].endRow) == int(currentObject.endRow) and int(initKList[Line].endCol) == int(currentObject.endCol):
                validCells = False
                print("Invalid End Cell")

            # Check if end cell == start cell
            elif int(initKList[Line].endRow) == int(currentObject.startRow) and int(initKList[Line].endCol) == int(currentObject.startCol):
                validCells = False
                print("INVALID Starting Cell")


    if (len(kList) > 0):
        for Line in range(len(kList)):

            # Check if start cell == start cell
            if int(kList[Line].startRow) == int(currentObject.startRow) and int(kList[Line].startCol) == int(currentObject.startCol):
                validCells = False
                print("INVALID Start Cell")

             # Check if the start cell == end cell
            if int(initKList[Line].startRow) == int(currentObject.endRow) and int(initKList[Line].startCol) == int(currentObject.endCol):
                validCells = False
                print("INVALID Starting Cell")

            # Check if end cell == end cell
            if int(kList[Line].endRow) == int(currentObject.endRow) and int(kList[Line].endCol) == int(currentObject.endCol):
                validCells = False
                print("INVALID End Cell")

            # Check if end cell == start cell
            if int(kList[Line].endRow) == int(currentObject.startRow) and int(kList[Line].endCol) == int(currentObject.startCol):
                validCells = False
                print("INVALID ending Cell")


    return validCells


def validateParallel(i):

    currentObject = objectList[i]
    currentIndex = i
    checkList = objectList[0:i]

    # Calculate Vector v1 for the current turn / line
    x1= int(currentObject.endRow) - int(currentObject.startRow)
    y1 = int(currentObject.endCol) - int(currentObject.startCol)

    for Line in range(currentIndex):
        # Calculate vector v2 for each comparison
        x2 = int(checkList[Line].endRow) - int(checkList[Line].startRow)
        y2 = int(checkList[Line].endCol) - int(checkList[Line].startCol)

        if x1 * y2 == x2 * y1:
            return True
        else:
            return False


def plotLine(i,turn):
    currentObject = objectList[i]
    currentIndex = i
    tValue = 0

    # Calcualte the vector of the line, for the parametric equation on the line
    v1 = (int(currentObject.endRow)-1) - (int(currentObject.startRow)-1)
    v2 = (int(currentObject.endCol)-1) - (int(currentObject.startCol)-1)

    # Find which value is larger for the tValue in the lines equation
    if v1 > v2:
        tValue = v1
    elif v1 < v2:
        tValue = v2
    elif v1 == v2:
        tValue = v1

    # calculate the points to be played on the board
    for t in range(tValue):
        nextRow = math.ceil(((t/tValue) * v1) + (int(currentObject.startRow))-1)
        nextCol = math.ceil(((t/tValue) * v2) + (int(currentObject.startCol))-1)

        gameBoard[nextRow,nextCol] = turn


def calculateScore(gameboard,endGame):
    playerXscore=0
    playerOscore=0

    #Iterate over ever cell
    for rows in gameboard:
        for i,cols in enumerate(rows):
            if rows[i] == 'X':
                playerXscore +=1
            elif rows[i] == 'O':
                playerOscore +=1

    if endGame == False:
        print("Player X score: ",playerXscore)
        print("Player O score: ",playerOscore)
    else:
        if playerOscore > playerXscore:
            print("Player O WINS with:", playerOscore , "points.")
        else:
            print("Player X WINS with:", playerXscore,"points.")
    return True


def remianingCells(gameboard):
    availableCellCount=0

    # Iterate over ever cell
    for rows in gameboard:
        for i, cols in enumerate(rows):
            if rows[i] == "-":
                availableCellCount +=1

    return availableCellCount


# Global variables. List to hold objects, n val and k val
objectList = []
nValue = 0
kValue = 0
file = input("Enter the name of the .txt file to read from (ex: input_files/pa2_input_1.txt): ")

# Read each line from the file, store data into objects and variables
with open(file, 'r') as f:
    firstLine = f.readline().split(" ")
    nValue = firstLine[0]
    kValue = int(firstLine[1])

    for vector in f:
        newTurn = Line()
        TempList = vector.split(" ")

        # Set start and end cells
        newTurn.set_startRow(TempList[0])
        newTurn.set_startCol(TempList[1])
        newTurn.set_endRow(TempList[2])
        newTurn.set_endCol(TempList[3])

        # Set midpoints
        newTurn.set_midpointCol(int(TempList[1]),int(TempList[3]))
        newTurn.set_midpointRow(int(TempList[0]),int(TempList[2]))

        objectList.append(newTurn)

# Create the Game board of size N x N
gameBoard = np.empty((int(nValue),int(nValue)), dtype=str)
gameBoard.fill('--')

# Iterate over the objectList[] of turns, one index at a time
# Play the valid lines
i = 0
length = len(objectList)
consecutiveInvalidTurns = 0

while i < length:

    # The first turn will always be valid
    if i == 0:
        gameBoard[int(objectList[i].startRow) - 1, int(objectList[i].startCol) - 1] = "O"
        plotLine(i, "O")
        gameBoard[int(objectList[i].endRow) - 1, int(objectList[i].endCol) - 1] = "O"
        print("Player O Turn: ")
        print(gameBoard)

    # Validate then play the rest of the player turns
    else:
        # Identify which player is going
        if i % 2:
            print("\nPlayer X Turn: ")
        else:
            print("\nPlayer O Turn: ")

        # Validate the midpoints do not intersect within kTurns
        print("Is the midpoint intersection valid? ",validateMidpoint(kValue,i))

        # Validate that the cells are empty
        print("Are the Start / End cells empty? ",validateCells(kValue,i))

        # Validate that the lines are not parallel
        print("Is the line parallel to other lines?: ",validateParallel(i))

        print("- - - - - -")

        # If the turn is valid, we will play the lines on the gameboard
        if validateMidpoint(kValue, i) is True and validateCells(kValue, i) is True and validateParallel(i) is False:

            if consecutiveInvalidTurns > 0:
                consecutiveInvalidTurns = consecutiveInvalidTurns - 1

            # If the index is odd, it is player 2's turn
            if i % 2:
                print("Valid Line")
                gameBoard[int(objectList[i].startRow)-1,int(objectList[i].startCol)-1] = "X"
                gameBoard[int(objectList[i].endRow)-1,int(objectList[i].endCol)-1] = "X"
                plotLine(i, "X")

            # if index is even, it is player 1's turn
            else:
                print("Valid Line")
                gameBoard[int(objectList[i].startRow)-1, int(objectList[i].startCol)-1] = "O"
                gameBoard[int(objectList[i].endRow)-1, int(objectList[i].endCol)-1] = "O"
                plotLine(i, "O")

            print("\n", gameBoard)

        # Turn is invalid, and will not be played
        else:
            consecutiveInvalidTurns = consecutiveInvalidTurns + 1
            if i % 2:
                print("INVALID Line ")
            else:
                print("INVALID Line ")

            print("\n", gameBoard)

    # Calculate players scores
    calculateScore(gameBoard,False)

    if remianingCells(gameBoard) > 0 and consecutiveInvalidTurns !=2:
        # Next turn?
        print("---------------------------")
        print("Would you like to move on? (y / n)")
        nextMove = input()

        if nextMove == 'Y' or nextMove == 'y':
            i += 1
    else:
        print("\nThere have been ", consecutiveInvalidTurns, " consecutive INVALID turns.\n--Game Over--\n")
        i = length

# End of game message
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
calculateScore(gameBoard, True)
print(gameBoard)

# Write final game board to file
matrixBoard = np.matrix(gameBoard)
outputFile = input("Please enter the name of the output file to write to: (ex: output_files/pa2_output_2.txt) ")
with open(outputFile, "w") as f:
    for line in matrixBoard:
        np.savetxt(f, line, fmt='%s')