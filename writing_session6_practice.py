# Adding and Deleting Shapes
from cmu_112_graphics import *
#1. Fill in each blank with Model, View, or Controller:
#viewToModel and modelToView
# A) The _____controller_______ responds to keyboard, mouse, timer and other events
# and updates the model.

 
# B) The ______views__________ draws the app using the values in the model.


# C) The _____model_____ contains all the data we need for the animation.


# D)  Controllers can only update the _______model_________, they cannot update
# the _____view___________.


# E)  The view can never call the controller functions, and the view also
# can never update the _______model_________.



# 2. Fill in the blanks with the appropriate values for event.key:

#     User types:                            event.key value:

#     The enter key (aka return)             ______'Enter'______

#     The space key (aka the space bar)      ____'Space'____________

#     The left arrow key                     _______'Left'_________

#     The # sign (shift-3)                   _____'#'__________


# 3. True or False:

# A) Your code never directly calls redrawAll (the view) or event handlers
# like keyPressed (the controllers) -- these are called for you by the
# animation framework. __True___

# B) An MVC Violation occurs if you try to update the model while drawing.
    #__True__ 
# C) If the user presses the mouse, the animation framework will first call 
# mousePressed (the controller), and when that call has completely finished,
# only then will the animation framework call redrawAll (the view).
    #__True__ 


# 4. Fill in the blank:

# A) If we set app.timerDelay to 50, then we will get roughly ________20______
# calls to timerFired per second.

# B) In our grid example, getCell is also known as ____viewToModel______,
# because it takes (x,y) values and converts them to row,col values.

# C) In our grid example, getCellBounds is also known as _modelToView_____,
# because it takes row,col values and converts them to (x,y) values.

#D) In our grid example, if we set app.rows and app.cols both to 2 in appStarted
# and then we clicked the mouse near the top-right corner of the canvas,
# then app.selection would be set to ___________(0,1)___________.


# 5. Very short answers:

# A) Consider this code excerpt from doStep in our bouncing square example:
#    if app.squareLeft < 0: 
#         # if so, reverse!
#         app.squareLeft = 0
#         app.dx = -app.dx 
# Very briefly, why do we set app.squareLeft = 0?
#To make it inside the bounds

# B) In our snake example, why do we use app.waitingForFirstKeyPress?
#we do not want the game to run until we enter a key 

# C) In our snake example, in takeStep, we check if 
# ((newRow, newCol) in app.snake)).
# Very briefly, what situation does this test for?
#checks if the area of the snake is moving into the snake's body. 

# D) In our snake example, placeFood includes a 'while' loop.  Very briefly,
# what is the purpose of this loop?
#To keep creating a new random position for the food until the position is 
#valid.     

# 6. In our snake example, mark each of the following with M, V, or C if it is
# from the Model, View, or Controller:

# A) app.foodPosition M
# B) app.rows M 
# C) drawSnake() V 
# D) app.snake M 
# E) app.cols M 
# F) drawGameOver() V 
# G) app.margin M 
# H) drawBoard() V 
# I) app.waitingForFirstKeyPress M 
# J) timerFired() C 
# K) app.direction  M
# L) drawFood() V 
# M) redrawAll() V 
# N) keyPressed() C 
# O) takeStep() C 
# P) placeFood() C 

def appStarted(app):
    app.circleCenters = [ ]

def mousePressed(app, event):
    newCircleCenter = (event.x, event.y)
    app.circleCenters.append(newCircleCenter)

def keyPressed(app, event):
    if (event.key == 'd'):
        if (len(app.circleCenters) > 0):
            app.circleCenters.pop(0)
        else:
            print('No more circles to delete!')

def redrawAll(app, canvas):
    # draw the circles
    for circleCenter in app.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='cyan')
    # draw the text
    canvas.create_text(app.width/2, 20,
                       text='Example: Adding and Deleting Shapes')
    canvas.create_text(app.width/2, 40,
                       text='Mouse clicks create circles')
    canvas.create_text(app.width/2, 60,
                       text='Pressing "d" deletes circles')

runApp(width=400, height=400)

# Grids
from cmu_112_graphics import *

def appStarted(app):
    app.rows = 4
    app.cols = 8
    app.margin = 5 # margin around grid
    app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none

def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows

    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)

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

def mousePressed(app, event):
    (row, col) = getCell(app, event.x, event.y)
    # select this (row, col) unless it is selected
    if (app.selection == (row, col)):
        app.selection = (-1, -1)
    else:
        app.selection = (row, col)

def redrawAll(app, canvas):
    # draw grid of cells
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "orange" if (app.selection == (row, col)) else "cyan"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    canvas.create_text(app.width/2, app.height/2 - 15, text="Click in cells!",
                       font="Arial 26 bold", fill="darkBlue")

runApp(width=400, height=400)

# Bouncing Square 
from cmu_112_graphics import *

def appStarted(app):
    app.squareLeft = app.width//2
    app.squareTop = app.height//2
    app.squareSize = 25
    app.dx = 10
    app.dy = 15
    app.isPaused = False
    app.timerDelay = 50 # milliseconds

def keyPressed(app, event):
    if (event.key == "p"):
        app.isPaused = not app.isPaused
    elif (event.key == "s"):
        doStep(app)

def timerFired(app):
    if (not app.isPaused):
        doStep(app)

def doStep(app):
    # Move horizontally
    app.squareLeft += app.dx

    # Check if the square has gone out of bounds, and if so, reverse
    # direction, but also move the square right to the edge (instead of
    # past it). Note: there are other, more sophisticated ways to
    # handle the case where the square extends beyond the edges...
    if app.squareLeft < 0:
        # if so, reverse!
        app.squareLeft = 0
        app.dx = -app.dx
    elif app.squareLeft > app.width - app.squareSize:
        app.squareLeft = app.width - app.squareSize
        app.dx = -app.dx
    
    # Move vertically the same way
    app.squareTop += app.dy 
    if app.squareTop < 0:
        # if so, reverse!
        app.squareTop = 0
        app.dy = -app.dy
    elif app.squareTop > app.height - app.squareSize:
        app.squareTop = app.height - app.squareSize
        app.dy = -app.dy

def redrawAll(app, canvas):
    # draw the square
    canvas.create_rectangle(app.squareLeft,
                            app.squareTop,
                            app.squareLeft + app.squareSize,
                            app.squareTop + app.squareSize,
                            fill="yellow")
    # draw the text
    canvas.create_text(app.width/2, 20,
                       text="Pressing 'p' pauses/unpauses timer")
    canvas.create_text(app.width/2, 40,
                       text="Pressing 's' steps the timer once")

runApp(width=400, height=150)

# Snake 

from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 5 # margin around grid
    app.timerDelay = 250
    initSnakeAndFood(app)
    app.waitingForFirstKeyPress = True

def initSnakeAndFood(app):
    app.snake = [(0,0)]
    app.direction = (0, +1) # (drow, dcol)
    placeFood(app)
    app.gameOver = False

# getCellBounds from grid-demo.py
def getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def keyPressed(app, event):
    if (app.waitingForFirstKeyPress):
        app.waitingForFirstKeyPress = False
    elif (event.key == 'r'):
        initSnakeAndFood(app)
    elif app.gameOver:
        return
    elif (event.key == 'Up'):      app.direction = (-1, 0)
    elif (event.key == 'Down'):  app.direction = (+1, 0)
    elif (event.key == 'Left'):  app.direction = (0, -1)
    elif (event.key == 'Right'): app.direction = (0, +1)
    # elif (event.key == 's'):
        # this was only here for debugging, before we turned on the timer
        # takeStep(app)

def timerFired(app):
    if app.gameOver or app.waitingForFirstKeyPress: return
    takeStep(app)

def takeStep(app):
    (drow, dcol) = app.direction
    (headRow, headCol) = app.snake[0]
    (newRow, newCol) = (headRow+drow, headCol+dcol)
    if ((newRow < 0) or (newRow >= app.rows) or
        (newCol < 0) or (newCol >= app.cols) or
        ((newRow, newCol) in app.snake)):
        app.gameOver = True
    else:
        app.snake.insert(0, (newRow, newCol))
        if (app.foodPosition == (newRow, newCol)):
            placeFood(app)
        else:
            # didn't eat, so remove old tail (slither forward)
            app.snake.pop()

def placeFood(app):
    # Keep trying random positions until we find one that is not in
    # the snake. Note: there are more sophisticated ways to do this.
    while True:
        row = random.randint(0, app.rows-1)
        col = random.randint(0, app.cols-1)
        if (row,col) not in app.snake:
            app.foodPosition = (row, col)
            return

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill='white')

def drawSnake(app, canvas):
    for (row, col) in app.snake:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='blue')

def drawFood(app, canvas):
    if (app.foodPosition != None):
        (row, col) = app.foodPosition
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='green')

def drawGameOver(app, canvas):
    if (app.gameOver):
        canvas.create_text(app.width/2, app.height/2, text='Game over!',
                           font='Arial 26 bold')
        canvas.create_text(app.width/2, app.height/2+40,
                           text='Press r to restart!',
                           font='Arial 26 bold')

def redrawAll(app, canvas):
    if (app.waitingForFirstKeyPress):
        canvas.create_text(app.width/2, app.height/2,
                           text='Press any key to start!',
                           font='Arial 26 bold')
    else:
        drawBoard(app, canvas)
        drawSnake(app, canvas)
        drawFood(app, canvas)
        drawGameOver(app, canvas)

runApp(width=400, height=400)