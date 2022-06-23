import numpy as np
outputFile = open("output.txt", "w")

# Parse the input file to obtain matrix of sudoku.
def parseInput(fileName):

    inputFile = open(fileName, "r")
    matrix = np.zeros([9,9], dtype=int)

    # Iterate through all lines in input file.
    for row, line in enumerate(inputFile.read().split("\n")):
        for column, input in enumerate(line.split(",")):

            # Fill matrix with input.
            if input == " ":
                matrix[row, column] = 0 
            else:
                matrix[row, column] = int(input)

    return matrix

# Obtain list of numbers in each grid.
def obtainGrids(matrix):
    grids = []

    # Obtain first row of grids of puzzle.
    for i in range(0, 9, 3):
        firstGrid = inputMatrix[i:i+3, 0:3].ravel().tolist()
        secondGrid = inputMatrix[i:i+3, 3:6].ravel().tolist()
        thirdGrid = inputMatrix[i:i+3, 6:9].ravel().tolist()
        gridList = [firstGrid, secondGrid, thirdGrid]

        # Remove 0s from the list.
        for index, grid in enumerate(gridList):
            grid = list(dict.fromkeys(grid))

            if 0 in grid:
                grid.remove(0)

            gridList[index] = grid

        grids.append(gridList)
    
    return grids

class Node:

    def __init__(self, matrix, xPos, yPos):

        self.visited = False
        self.matrix = matrix 

        # The current position being calculated.
        self.coord = (xPos, yPos)

        # Possible outcomes for the current position.
        self.children = []

    # Calculate the possible numbers for the next child.
    def prunePossibleNumbers(self, gridMatrix):
        possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Calculate which grid the current number is in.
        gridPos = (self.coord[0] // 3, self.coord[1] // 3)

        # Remove numbers from possibleNumbers if they are in the same grid.
        [possibleNumbers.remove(x) for x in gridMatrix[gridPos[0]][gridPos[1]]]

        # Remove numbers from possible numbers if they are in the same row.
        [possibleNumbers.remove(x) for x in self.matrix[self.coord[0]] if x in possibleNumbers]
        print(possibleNumbers)
        # Remove numbers from possible numbers if they are in the same column.
        # print(possibleNumbers)
        return possibleNumbers

    def createChildren(self):
        pass

inputMatrix = parseInput("testInput.txt")
sudokuGrids = obtainGrids(inputMatrix)
node = Node(inputMatrix, 0, 2)
node.prunePossibleNumbers(sudokuGrids)
# print(sudokuGrids)