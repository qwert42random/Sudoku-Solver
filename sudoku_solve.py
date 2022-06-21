import numpy as np
outputFile = open("output.txt", "w")

# Parse the input file to obtain matrix of sudoku.
def parseInput(fileName):

    inputFile = open(fileName, "r")
    matrix = []
    matrix_line = []

    # Iterate through all lines in input file.
    for line in inputFile.read().split("\n"):

        for char in line.split(","):

            # If space, then None. Otherwise, is number.
            if char == " ":
                matrix_line.append(None)
            else:
                matrix_line.append(int(char))

        matrix.append(matrix_line)
        matrix_line = []

    return np.matrix(matrix)

inputMatrix = parseInput("testInput.txt")
print(inputMatrix)
print()

# Print first row of grids of puzzle.
for i in [0, 3, 6]:
    print(inputMatrix[i:i+3, 0:3])
    print()
