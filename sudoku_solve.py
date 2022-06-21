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

def obtainGrids(matrix):
    grids = []

    # Print first row of grids of puzzle.
    for i in range(0, 9, 3):
        grids.append([inputMatrix[i:i+3, 0:3], inputMatrix[i:i+3, 3:6], inputMatrix[i:i+3, 6:9]])
    
    return grids

inputMatrix = parseInput("testInput.txt")
sudokuGrids = obtainGrids(inputMatrix)
print()
print(sudokuGrids)

exit()

# Print second row of grids of puzzle.
for i in [0, 3, 6]:
    print(inputMatrix[3:6, i:i+3])
    print()

# Print third row of grids of puzzle.
for i in [0, 3, 6]:
    print(inputMatrix[6:9, i:i+3])
    print()

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class node:
    def __init__(self, matrix):
        self.visited = False
        self.possibleNumbers = []
        self.matrix = matrix 
        self.x = None
        self.y = None
        self.children = []
        pass
