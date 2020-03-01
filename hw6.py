#################################################
# hw6.py: Tetris!
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2 
#################################################

import cs112_s20_unit6_linter
import math, copy, random

from cmu_112_graphics import *

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

#################################################
# Functions for you to write
#################################################

#initialize our variables
def gameDimensions(): 
    rows = 15
    cols = 10 
    cellSize = 20 
    margin = 25
    return (rows, cols, cellSize, margin)

#this function gets the bounds of two cells 
# from : https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    columnWidth = gridWidth / app.cols
    rowHeight = gridHeight / app.rows
    x0 = app.margin + col * columnWidth
    x1 = app.margin + (col+1) * columnWidth
    y0 = app.margin + row * rowHeight
    y1 = app.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)

#helper function that declares the type of pieces we can have in tetris 
def declarePieces(): 
    iPiece = [
        [  True,  True,  True,  True ]
    ]
    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]
    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ] 
    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]
    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]
    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]
    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    return iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece

#initialize all our varibales for the app that we need to start coding the app 
def appStarted(app):
    app.score = 0
    app.isGameOver = False
    app.emptyColor = "blue" 
    app.rows, app.cols, app.cellSize, app.margin = gameDimensions()
    app.board = [[0]*app.cols for r in range(app.rows)]
    for r in range(app.rows): 
        for c in range(app.cols):
            app.board[r][c] = app.emptyColor

    # Seven "standard" pieces (tetrominoes)

    (app.iPiece, app.jPiece, app.lPiece, app.oPiece, app.sPiece, app.tPiece,
    app.zPiece) = declarePieces()

    tetrisPieces = [app.iPiece, app.jPiece, app.lPiece, 
    app.oPiece, app.sPiece, app.tPiece, app.zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green",
    "orange" ]

    app.tetrisPieces = tetrisPieces
    app.tetrisPieceColors = tetrisPieceColors

    newFallingPiece(app)

#function draws a cell of the board
def drawCell(app, canvas, row, col, color):
    x1, y1, x2, y2 = getCellBounds(app, row, col) 
    canvas.create_rectangle(x1, y1, x2, y2, fill = color, width = 3)

#this function draws the board of tetris
def drawBoard(app, canvas):
    for c in range(app.cols): 
        for r in range(app.rows): 
            drawCell(app, canvas, r, c, app.board[r][c])

#creates a new falling piece for the game: defines the num of cols and rows, 
#left most col and row 
def newFallingPiece(app): 
    import random 
    randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
    app.fallingPiece = app.tetrisPieces[randomIndex]
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex]
    app.numFallingPieceCols = len(app.fallingPiece[0])
    app.numFallingPieceRows = len(app.fallingPiece)
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols//2 - app.numFallingPieceCols//2 
#draws the falling piece using the data from newFallingPiece
def drawFallingPiece(app, canvas): 
    fallingPieceRows = len(app.fallingPiece)
    fallingPieceCols = len(app.fallingPiece[0])

    for r in range(fallingPieceRows): 
        for c in range(fallingPieceCols): 
            if app.fallingPiece[r][c] == True: 
                drawCell(app, canvas, r + app.fallingPieceRow
                , c + app.fallingPieceCol, app.fallingPieceColor)

#set what is going to happen every time we hit a different key       
def keyPressed(app, event):
    if app.isGameOver: 
        if event.key == "r": 
            appStarted(app)
    elif not app.isGameOver: 
        if event.key == "Up": 
            rotateFallingPiece(app)
        elif event.key == "Down":
            moveFallingPiece(app, 1, 0)
        elif event.key == "Left":   
            moveFallingPiece(app, 0, -1)
        elif event.key == "Right": 
            moveFallingPiece(app, 0, 1)
        elif event.key == "Space": 
            hardDrop(app)

#function that drops the piece when the space is clicked
def hardDrop(app): 
    while moveFallingPiece(app, 1, 0): pass
    placeFallingPiece(app)
#function to be able to move the position of a fallingPiece
def moveFallingPiece(app, drow, dcol): 
    app.pieceMoved = True 
    app.fallingPieceRow += drow
    app.fallingPieceCol += dcol 
    if not fallingPieceIsLegal(app):
        app.pieceMoved = False
        app.fallingPieceRow -= drow 
        app.fallingPieceCol -= dcol
    return app.pieceMoved

#function to check if the falling piece is legal or not 
def fallingPieceIsLegal(app): 
    for r in range(len(app.fallingPiece)): 
        for c in range(len(app.fallingPiece[0])):
            if  app.fallingPiece[r][c] == True:
                if (c + app.fallingPieceCol >= app.cols
                or r + app.fallingPieceRow >= app.rows or
                c + app.fallingPieceCol < 0 or r + app.fallingPieceRow < 0 or 
                app.board[app.fallingPieceRow + r][app.fallingPieceCol + c] != 
                app.emptyColor): 
                    return False 
    return True

#function that is used to rotate 90 degrees the falling piece 
def rotateFallingPiece(app): 
    app.rotateFallingPieceRows = len(app.fallingPiece[0]) 
    app.rotateFallingPieceCols = len(app.fallingPiece)
    app.rotateFallingPiece = [[None]*app.rotateFallingPieceCols for r 
    in range(app.rotateFallingPieceRows)]
    for r in range(app.rotateFallingPieceRows): 
        for c in range(app.rotateFallingPieceCols): 
            app.rotateFallingPiece[r][c] = app.fallingPiece[-c-1][r]
        
    app.recordFallingPiece =  app.fallingPiece
    app.fallingPiece = app.rotateFallingPiece

    if fallingPieceIsLegal(app): 
        oldRow = app.fallingPieceRow
        oldCol = app.fallingPieceCol
    
        newFallingPieceRow = (oldRow + len(app.fallingPiece)//2 
        - app.rotateFallingPieceRows//2)
    
        newFallingPieceCol = (oldCol + len(app.fallingPiece[0])//2 
        - app.rotateFallingPieceCols//2)
        app.fallingPieceRow = newFallingPieceRow 
        app.falligPieceCol = newFallingPieceCol
    else:
        app.fallingPiece = app.recordFallingPiece

#this function stops the falling piece from moving once it reaches the end 
def placeFallingPiece(app): 
    fallingPieceRows = len(app.fallingPiece)
    fallingPieceCols = len(app.fallingPiece[0])
    for r in range(fallingPieceRows): 
        for c in range(fallingPieceCols): 
            if app.fallingPiece[r][c] == True: 
                app.board[r + app.fallingPieceRow][c + app.fallingPieceCol] = \
                app.fallingPieceColor
    removeFullRows(app) 

def removeFullRows(app): 
    prevBoardRows = len(app.board)
    prevBoardCols = len(app.board[0])
    fullRows = 0 
    #creates a list with the color blue for the empty rows
    emptyRow = [app.emptyColor]*prevBoardCols
    for r in range(prevBoardRows): 
        if app.emptyColor not in app.board[r]: 
            fullRows += 1 
            #if there is no blue the row is full and then we pop the row and 
            #insert a new row
            app.board.pop(r)
            app.board.insert(0, emptyRow)
        app.score += fullRows**2 

#draws the current score of the game at the top of the board 
def drawScore(app, canvas): 
    canvas.create_text(app.width//2 , app.margin//2, fill = "blue", 
    font = "Arial 12 bold", text = f'Score: {app.score}')

def timerFired(app): 
    if app.isGameOver: return
    if not moveFallingPiece(app, 1, 0): 
        placeFallingPiece(app) 
        newFallingPiece(app)
        if not fallingPieceIsLegal(app): 
            app.isGameOver = True 
            
def redrawAll(app, canvas): 
    canvas.create_rectangle(0,0, app.width, app.height, fill = "orange")
    drawBoard(app,canvas)
    drawFallingPiece(app, canvas)
    drawScore(app, canvas)
    if app.isGameOver : 
        canvas.create_rectangle(app.margin, app.height//2 - app.margin,
        app.width- app.margin, app.height//1.5 - app.margin, fill = "black")
        canvas.create_text(app.width//2 , app.height//2 + 2, 
        font = "Arial 20 bold", text = "Game Over!", fill = "yellow")
        return
        
def playTetris():
    rows, cols, cellSize, margin = gameDimensions()
    width = cellSize*cols + 2*margin
    height = cellSize*rows + 2*margin
    runApp(width = width, height = height)


#################################################
# main
#################################################

def main():
    cs112_s20_unit6_linter.lint()
    playTetris()

if __name__ == '__main__':
    main()