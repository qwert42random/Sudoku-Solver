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
        self.complete = False
        self.matrix = matrix
        self.sudokuGrids = self.obtainGrids()

        # The current position being calculated.
        self.coord = (xPos, yPos)

        # Possible outcomes for the current position.
        self.children = []


    # Calculate the possible numbers for the next child.
    def prunePossibleNumbers(self):

        possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Calculate which grid the current number is in.
        gridPos = (self.coord[0] // 3, self.coord[1] // 3)

        # Remove numbers from possibleNumbers if they are in the same grid.
        [possibleNumbers.remove(x) for x in self.sudokuGrids[gridPos[0]][gridPos[1]]]

        # Remove numbers from possible numbers if they are in the same row.
        [possibleNumbers.remove(x) for x in self.matrix[self.coord[1]] if x in possibleNumbers]

        # Remove numbers from possible numbers if they are in the same column.
        [possibleNumbers.remove(x) for x in self.matrix[0:, self.coord[0]] if x in possibleNumbers]

        return possibleNumbers

    def createChildren(self):
        possibleAnswers = self.prunePossibleNumbers()

        # Find the next empty space.
        nextPos = [self.coord[0], self.coord[1]]
        pointer = None

        # Find next empty space.
        while pointer != 0:

            # Iterate accross column to find next empty space. If end of column, go down a row.
            if nextPos[0] + 1 > 8:
                nextPos[0] = 0
                nextPos[1] += 1
            else:
                nextPos[0] += 1

            # No other empty space on sudoku grid.
            if nextPos[0] > 8:
                self.complete = True
                return

            pointer = self.matrix[nextPos[1], nextPos[0]]

        # Iterate through all possible answers.
        for answer in possibleAnswers:

            # Create a matrix with the possible answer in place.
            childMatrix = self.matrix.copy()
            childMatrix[self.coord[1]][self.coord[0]] = answer

            # Create new node with updated matrix. 
            childNode = Node(childMatrix, nextPos[0], nextPos[1])
            self.children.append(childNode)

def traverseGraph(currentNode):

    # Create the children of the current node.
    currentNode.createChildren()

    # Iterate through children of the node.
    for children in currentNode.children:

        # print(children.coord)

        if children.complete == True:
            print("Finished")
            print(children.matrix)
        elif children.visited == False:
            children.visited = True
            traverseGraph(children)

# Main code.
if __name__ == "__main__":
    inputMatrix = parseInput("testInput.txt")
    node = Node(inputMatrix, 2, 0)
    node.createChildren()
    # print([(children.coord, index) for index, children in enumerate(node.children)])
    traverseGraph(node)
    pass
