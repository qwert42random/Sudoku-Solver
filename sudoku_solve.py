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


class Node:

    # Obtain list of numbers in each grid.
    def obtainGrids(self):
        grids = []

        # Obtain first row of grids of puzzle.
        for i in range(0, 9, 3):
            firstGrid = self.matrix[i:i+3, 0:3].ravel().tolist()
            secondGrid = self.matrix[i:i+3, 3:6].ravel().tolist()
            thirdGrid = self.matrix[i:i+3, 6:9].ravel().tolist()
            gridList = [firstGrid, secondGrid, thirdGrid]

            # Remove 0s from the list.
            for index, grid in enumerate(gridList):
                grid = list(dict.fromkeys(grid))

                if 0 in grid:
                    grid.remove(0)

                gridList[index] = grid

            grids.append(gridList)
        
        return grids

    def __init__(self, matrix, xPos, yPos):

        self.visited = False
        self.matrix = matrix
        self.sudokuGrids = self.obtainGrids()

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
        [possibleNumbers.remove(x) for x in self.matrix[self.coord[1]] if x in possibleNumbers]

        # Remove numbers from possible numbers if they are in the same column.
        [possibleNumbers.remove(x) for x in self.matrix[0:, self.coord[0]] if x in possibleNumbers]

        return possibleNumbers

    def createChildren(self):
        pass


# Main code.
if __name__ == "__main__":
    inputMatrix = parseInput("testInput.txt")
    node = Node(inputMatrix, 3, 0)
    print(node.sudokuGrids)
    node.createChildren()
    # print(sudokuGrids)
    pass
