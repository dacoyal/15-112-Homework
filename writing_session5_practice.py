#################################################
# writing_session5_practice_solutions.py
#################################################

import cs112_s20_unit5_linter
import math, copy

#################################################
# Helper functions
#################################################
# #1. Which of the following correctly creates a 3x2 (3 rows, 2 columns) 2d list
#    without any aliases?
#   A) [ [0] * 2 ] * 3
#   B) [ [0] * 3 ] * 2
#-->C) [ ([0] * 2) for i in range(3) ]
#   D) [ ([0] * 3) for i in range(2) ]
#   E) None of the above

# 2. If we had a non-ragged 3d list L (so "cubic" instead of "rectangular"),
#    which of the following would return all 3 dimensions:
#   A) len(L), len(L[0]), len(L[0,0])
#-->B) len(L), len(L[0]), len(L[0][0])
#   C) len(L), len(L[0]), len(L[-1])
#   D) len(L[0]), len(L[0][0]), len(L[0][0][0])
#   E) None of the above

# 3. Why should we use use copy.deepcopy instead of copy.copy on 2d lists?
#   A) copy.copy has a bug and crashes on 2d lists
#-->B) copy.copy creates a shallow copy with aliases to the inner lists
#   C) copy.copy is much slower than copy.deepcopy
#   D) copy.copy works the same as copy.deepcopy on 2d lists
#   E) None of the above

# 4. Why did we provide our own myDeepCopy in the notes?
#-->A) copy.deepcopy is very slow, ours is much faster
#   B) copy.deepcopy is not available on some versions of Python
#   C) copy.deepcopy will preserve existing aliases in a 2d list, ours will not
#   D) copy.deepcopy is not a preferred way to copy a 2d list
#   E) None of the above

# 5. Why did we provide our own print2dList in the notes?
#   A) The builtin print2dList function works poorly in some cases
#-->B) There is no builtin print2dList function and just printing a 2d list
#      makes it appear on a single line and also does not align the columns,
#      and thus makes it hard to read.

# 6. What happens if we reverse the order of the 'for' loops in the standard
#    way we loop over a 2d list L.  That is, what if instead of this:

#             for row in range(rows):
#                 for col in range(cols):

# we did this:

#             for col in range(cols):
#                 for row in range(rows):

#   A) We would skip some of the values in L
#   B) We would visit all the values in row 0 first, then row 1, and so on
#-->C) We would visit all the values in col 0 first, then col 1, and so on
#   D) This code will not run at all
#   E) None of the above

# 7. Which of the following does NOT set M to a list of the values in column c
#    of the 10x10 2d list L?
#   A) M = [ L[i][c] for i in range(10) ]
#   B) N, M = copy.deepcopy(L), [ ]
#      while (N != [ ]):
#          M.append(N.pop(0)[c])
#-->C) M = [ ]
#      for i in range(10):
#          M += [ L[c][i] ]
#   D) None of the above


# import copy

# def ct():
#     # fill in each space to the right of each print statement
#     # with the value it prints

#     a = [[1]]
#     b = copy.copy(a)
#     c = copy.deepcopy(a)
#     b.append(2)
#     c.append([3])
#     print(a, b, c)           # [[1]] [[1], 2] [[1], [3]]

#     a = [[4,5]] * 2
#     b = copy.deepcopy(a)
#     a[1][1] = 6
#     print(a,b)              # [[4, 6], [4, 6]] [[4, 5], [4, 5]]

#     a = [[1,2],[3,4]]
#     b = a[::-1]
#     c = [r[::-1] for r in a]
#     print(b, c)             # [[3, 4], [1, 2]] [[2, 1], [4, 3]]

#     a = [[1,2,3],[4,5,6]]
#     for c in range(len(a[0])):
#         for r in range(c):
#             a[r][c] *= 10
#     print(a)                # [[1, 20, 30], [4, 5, 60]]

#     a = [[1,2],[3],[4,5,6]]
#     b = [ ]
#     for r in range(len(a)):
#         b += [len(a[r])]
#     print(b)                ## [2, 1, 3] 
5
# ct()


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

#################################################
# Functions for you to write
#################################################

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    result = [] 
    rows, cols = len(A), len(A[0])
    for r in range(rows): 
        if r != row: 
            newRow = [] 
            for c in range(cols): 
                if c!= col: 
                    newRow.append(A[r][c])
            result.append(newRow)
    return result

def destructiveRemoveRowAndCol(A, row, col):
    A.pop(row)
    rows = len(A) 
    for i in range(rows): 
        A[i].pop(col)

def bestQuiz(a):
    #there is only 2 rows(2 students), 3 colums (3 quizzes)
    currentAverage = 0 
    bestAverage = 0 
    numOfScores = 0 
    bestQuiz = None
    for c in range(len(a[0])): 
        currSum = 0
        numOfScores = 0 
        for r in range(len(a)):
            if (a[r][c] != -1):
                numOfScores += 1
                currSum += a[r][c] 
        if numOfScores > 0:
            currentAverage = currSum/numOfScores
            if currentAverage > bestAverage: 
                bestAverage = currentAverage
                bestQuiz = c
    return bestQuiz

def matrixAdd(L, M):
    rowsM, colsM = len(M), len(M[0])
    rowsL, colsL = len(L), len(L[0])
    if rowsL != rowsM or colsM != colsL: 
        return None
    result = copy.deepcopy(M)
    
    for r in range(rowsM):
        for c in range(colsM): 
            result[r][c] = M[r][c] + L[r][c] 
    return result

def isMostlyMagicSquare(a):
    firstDiagonal = []
    secondDiagonal = []
    cols = len(a[0])
    rows = len(a)
    sumHorizontals = 0
    previousSum = 0 
    currentSum = 0 
    previousSum1 = 0 
    currentSum1 = 0 
    for r in range(rows):
        previousSum = currentSum
        currentSum = 0  
        for c in range(cols):  
            currentSum += a[r][c]
        if previousSum != currentSum and r > 0 :
            return False 
    
    for c in range(cols): 
        previousSum1 = currentSum1
        currentSum1 = 0 
        for r in range(rows): 
            currentSum1 += a[r][c] 
        if previousSum1 != currentSum1 and c>0 : 
            return False 

    for n in range(len(a)):  
        firstDiagonal.append(a[n][n])
        secondDiagonal.append(a[n][len(a) - n - 1])
    return sum(firstDiagonal) == sum(secondDiagonal) 

class DataTable(object):
    def __init__(self, csvData):
        # load the 2d list from the csv string
        self.data = [] 
        csvData = csvData.strip() 
        for line in csvData.splitlines(): 
            line = line.strip() 
            items = line.split(',')
            self.data.append(items)
        
    def getDims(self): 
        rows = len(self.data)
        cols = len(self.data[0])
        return rows, cols
        
    def getColumn(self, colIndex): 
        colData = []
        for row in self.data: 
            colData.append(row[colIndex])
        label = colData[0]
        data = colData[1:]
        for i in range(len(data)): 
            if data[i].isdigit(): 
                data[i] = int(data[i])
            else: 
                data[i] = str(data[i])
        return DataColumn(label,data)
class DataColumn(object): 
    def __init__(self,label,data): 
        self.label = label 
        self.data = data

    def average(self): 
        return sum(self.data)/len(self.data)
#################################################
# Test Functions
#################################################

def testNondestructiveRemoveRowAndCol():
    print('Testing removeRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testBestQuiz():
    print('Testing bestQuiz()...', end='')
    a = [ [ 88,  80, 91 ],
          [ 68, 100, -1 ]]
    aCopy = copy.copy(a)
    assert(bestQuiz(a) == 2)
    assert(a == aCopy) # must be non-destructive!
    a = [ [ 88,  80, 80 ],
          [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88, -1, -1 ],
          [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1, -1, -1 ],
          [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    assert(bestQuiz([[]]) == None)
    print('Passed')

def testMatrixAdd():
    print('Testing matrixAdd()...', end='')
    L = [ [1,  2,  3],
          [4,  5,  6] ]
    M = [ [21, 22, 23],
          [24, 25, 26]]
    N = [ [1+21, 2+22, 3+23],
          [4+24, 5+25, 6+26]]
    lCopy = copy.copy(L)
    mCopy = copy.copy(M)
    assert(matrixAdd(L, M) == N)
    assert((L == lCopy) and (M == mCopy)) # must be non-destructive!
    assert(matrixAdd(L, [ [ 1, 2, 3] ]) == None) # dimensions mismatch
    print('Passed!')

def testIsMostlyMagicSquare():
    print("Testing isMostlyMagicSquare()...", end="")
    assert(isMostlyMagicSquare([[42]]) == True)
    assert(isMostlyMagicSquare([[2, 7, 6],
                                [9, 5, 1],
                                [4, 3, 8]]) == True)
    assert(isMostlyMagicSquare([[4-7, 9-7, 2-7],
                                [3-7, 5-7, 7-7],
                                [8-7, 1-7, 6-7]]) == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMostlyMagicSquare(a))
    assert(isMostlyMagicSquare([[1, 2], [2, 1]]) == False) # bad diagonals!
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMostlyMagicSquare(a) == False) # it's close, but not quite!
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMostlyMagicSquare(a) == False) # ditto!
    print("Passed!")

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))

    column0 = dataTable.getColumn(0)
    assert(isinstance(column0, DataColumn))
    assert(column0.label == 'Name')
    assert(column0.data == ['Fred', 'Wilma'])

    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testMatrixAdd()
    testIsMostlyMagicSquare()
    testDataTableAndDataColumnClasses()

def main():
    cs112_s20_unit5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
