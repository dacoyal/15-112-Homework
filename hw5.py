#################################################
# hw5.py
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2
#################################################

import cs112_s20_unit5_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

import copy
#function from : https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen
#function from : https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print([])
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print("[ ", end="")
    for row in range(rows):
        if (row > 0): print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if (col > 0): print(", ", end="")
            # The next 2 lines print a[row][col] with the given fieldWidth
            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][col]), end="")
        print(" ]", end="")
    print("]")

# function from: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)

#################################################
# Functions for you to write
#################################################

class CokeMachine(object):
    def __init__(self, bottleCount, bottleCost):
        self.bottleCount = bottleCount 
        self.bottleCost = bottleCost
        self.paidValue = 0
        self.change = 0 
    
    def getBottleCount(self): 
        return self.bottleCount 
    
    def getBottleCost(self): 
        return self.bottleCost
    
    def isEmpty(self): 
        if self.bottleCount != 0: 
            return False
        return True
    
    def insert(self, paidValue): 
        self.paidValue += paidValue
        #self.difference represents if we have paid more, less, or equal
        self.difference = self.bottleCost - self.paidValue
        #this checks if the cokeMachine is empty and if it is it changes change
        # to our desired -999 as well as the paid value to 0 .
        if self.isEmpty() == True: 
                self.paidValue = 0 
                self.change = -999
                return self.change 
        # this checks if the difference is greater than 0 means we have not paid
        # enough so change equals -1.
        if self.difference > 0: 
            self.change = -1
        # this checks if we have overpaid and if we have it sets the change to 
        # the absolute value of our difference. It also reduces the bottleCount 
        # since this would mean that we have succesfully bought a coke bottle .
        elif self.difference < 0: 
            self.change = abs(self.difference)
            self.bottleCount -= 1 
            self.paidValue = 0

        elif self.difference == 0: #if it is 0 
            self.change = 0 
            self.bottleCount -= 1
            self.paidValue = 0
        
        return self.change

    def stillOwe(self): 
        if self.change == -1 : 
            return self.bottleCost - self.paidValue
        else: 
            return self.bottleCost 
        
    def getPaidValue(self):
        return self.paidValue
    
    def addBottles(self, extraBottles): 
        self.bottleCount += extraBottles

#function from: https://www.cs.cmu.edu/~112/notes/unit5-case-studies.html
#edited some of the code to make it work for numbers
def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if ((drow != 0) or (dcol != 0)):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (str(board[row][col]) != word[i])):
            return None
    return ((startRow, startCol))

def isKingsTour(board):     
    rows, cols = len(board), len(board[0])
    numOfNumbers = rows*cols 
    #checks for the current number and next number in the board using wordSearch
    #to see if they are next to each other(wordSearch checks horizontally, 
    # vertically and diagonally) 
    for i in range(1, numOfNumbers):
        if (wordSearch(board, str(i) + str(i + 1)) == None):
            return False
    return True
    
def areLegalValues(values):   
    NSquared = len(values)
    #this loop makes sure no number is bigger than NSquared
    for c in values: 
        if c > NSquared: 
            return False 

   #this loop checks that the numbers are not repeated  
    for i in range(1,NSquared + 1):
        count = 0
        for c in values: 
            if i == c: 
                count += 1 
                if count > 1: 
                    return False 
    return True  
# this function checks if the row is legal      
def isLegalRow(board, row): 
    currentRow = board[row]
    return areLegalValues(currentRow)

def isLegalCol(board, col):
    currentCol = []
    rows = len(board)
    #make a new list that contains all the values of the column
    for i in range(rows): 
        currentCol.append(board[i][col])
    return areLegalValues(currentCol)

def isLegalBlock(board, block): 
    #there is N blocks per row 
    NSquared = len(board)
    #we need to get the initialCol and finalCol of the block to be able to get
    #the list of the numbers containing the values of block 
    N = int(math.sqrt(NSquared)) 
    initialRow = (block// (N)) * N
    finalRow = initialRow + N 
    initialCol = (block % (N)) * N
    finalCol = initialCol + N

    listOfBlock = []
    for r in range(initialRow, finalRow): 
        for c in range(initialCol, finalCol): 
            listOfBlock.append(board[r][c])

    return areLegalValues(listOfBlock)

def isLegalSudoku(board):
    NSquared = len(board)
    rows, cols = len(board), len(board[0])
    # loop through all the rows, cols, and blocks to make sure that all of them 
    #are legal 
    for r in range(rows):
        if not isLegalRow(board, r):
                return False 
        for c in range(cols): 
            if not isLegalCol(board, c): 
                return False 
    for block in range(NSquared):
        if not isLegalBlock(board, block): 
            return False 

    return True
           
#################################################
# Test Functions
#################################################
def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assert isLegalSudoku(board) == True
    board = [[1]]
    assert isLegalSudoku(board) == True

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assert isLegalSudoku(board) == False

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert isLegalSudoku(board) == True
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ]
    ]
    assert isLegalSudoku(board) == False
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assert isLegalSudoku(board) == True
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assert isLegalSudoku(board) == False
    print("Passed!!!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    a = [ [  3, 2, 1 ],
          [  6, 4, 9 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  2, 8, 9 ],
          [  3, 1, 7 ],
          [  4, 5, 6 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
    assert(isKingsTour(a) == False)
    a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    print("Passed!")

def testCokeMachineClass():
    print('Testing CokeMachine class...', end='')
    cm1 = CokeMachine(100, 125) # make a CokeMachine holding 100 bottles
                                # that each cost 125 cents ($1.25)
    assert(cm1.getBottleCount() == 100)
    assert(cm1.isEmpty() == False)
    assert(cm1.getBottleCost() == 125)  # $1.25 (125 cents)
    assert(cm1.getPaidValue() == 0)     # starts with no coins inserted

    # insert a dollar
    change = cm1.insert(100)  # we paid $1.00, it costs $1.25, so change == -1
                              # to indicate that not only is there no change,
                              # but we still owe money
    assert(change == -1)
    assert(cm1.stillOwe() == 25)

    # insert a dime more
    change = cm1.insert(10)
    assert(change == -1)
    assert(cm1.stillOwe() == 15)

    # and insert a quarter more.  Here, we finally pay enough, so we get a
    # bottle and some change!
    change = cm1.insert(25)
    assert(change == 10)
    assert(cm1.stillOwe() == 125)      # this is for the NEXT bottle
    assert(cm1.getBottleCount() == 99) # because we just got one!

    # second instance
    cm2 = CokeMachine(2, 50) # 2 bottles, $0.50 each

    # buy a couple bottles
    change = cm2.insert(25)
    assert(change == -1)
    assert(cm2.stillOwe() == 25)
    change = cm2.insert(25)
    assert(change == 0) # bought with exact change
    assert(cm2.isEmpty() == False)
    assert(cm2.getBottleCount() == 1)
    change = cm2.insert(100) # overpaid by $0.50
    assert(change == 50)
    assert(cm2.isEmpty() == True)
    assert(cm2.getBottleCount() == 0)

    # cannot buy anything more -- the machine is empty.
    # this is signified by returning -999 as the change
    change = cm2.insert(50)
    assert(change == -999)
    assert(cm2.isEmpty() == True)
    assert(cm2.getBottleCount() == 0)

    # addBottles method
    cm2.addBottles(50)
    assert(cm2.isEmpty() == False)
    assert(cm2.getBottleCount() == 50)
    change = cm2.insert(50)
    assert(change == 0)
    assert(cm2.getBottleCount() == 49)

    # independence of two instances
    assert(cm1.getBottleCount() == 99)
    assert(cm2.getBottleCount() == 49)

    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # required
    testCokeMachineClass()

    # mild
    testIsKingsTour()

    # medium
    testIsLegalSudoku()

    # spicy
    # Note that playSimplifiedChess is manually graded
    # so there is no test function for it.

def main():
    cs112_s20_unit5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
