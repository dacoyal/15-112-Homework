#################################################
# .py
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2
#################################################

import cs112_s20_unit2_linter
import basic_graphics
import math

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

def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

#################################################
# Functions f or you to write
#################################################
def drawFancyWheel(canvas, cx, cy, r, n, color): #this draws just ONE wheel
    #(x1,y1,x2,y2)
    #draws individual wheel 
    theta = math.pi/2
    dTheta = (2*math.pi) / n
    #calculate color  
    #how to return circle too ?
    canvas.create_oval(cx -r ,cy - r ,cx +r,cy + r, outline = color, width =2) 
    for point1 in range(n):
        x1 = (cx + r*math.cos(theta + point1*dTheta)) 
        y1 = (cy - r*math.sin(theta + point1*dTheta))
        for point2 in range(0,n):
            theta2 = theta + dTheta*point2
            x2, y2 = cx + r*math.cos(theta2), cy - r*math.sin(theta2)
            canvas.create_line(x1, y1, x2, y2, fill = color, width = 1.5)

def drawFancyWheels(canvas, width, height, rows, cols):
    #has to draw all the wheels
    numVertices = 4 + rows + cols 
    widthCell = width // cols
    heightCell = height // rows 
    rowCounter = 0 
    heightCounter = 0 
    for h in range(0, height,heightCell): 
        heightCounter += 1 
        rowCounter = 0 
        for w in range(0, width, widthCell): 
            rowCounter += 1
            if(rows == 1): 
                red = 0 
            else: 
                red = int((255/(rows-1)) * (heightCounter - 1))
            if(cols == 1):
                green = 255 
            else: 
                green = int(255 - 255/(cols -1)* (rowCounter -1))
            blue = 0 
            drawFancyWheel(canvas, widthCell/2 + w, heightCell/2 + h,
            widthCell/2 * 0.9, 4 + (rowCounter - 1) + (heightCounter - 1),
            rgbString(red, green, blue))

def drawBoard(canvas,width,height,rows,cols): 
    widthCell = width/cols
    heightCell = height/rows
    for row in range (rows): 
        for col in range(cols): 
            if (col + row) % 2 == 0:
                squareColor = rgbString(0,0,0) 
                circleColor = 'Red'
            else: 
                squareColor == 'Red' 
                circleColor = rgbString(0,0,0) 
        x0 = widthCell*col 
        y0 = heightCell*row 
        x0 = widthCell*(col + 1)
        y1 = heightCell*(row + 1)
        canvas.create_rectangle(x0,y0,x1,y1, fill = squareColor)
        canvas.create_oval(x0,y0,x1,y1, fill = circleColor, outline = 'White', 
        width = 3)


 #int(abs(-255/(rowCounter +1) + 255))
 #int(255 - 255/heightCounter)
def countDigits(n): 
    n = abs(n)
    if n < 10: 
        return 1
    length = 0 
    while(n > 0): 
        n //= 10 
        length += 1 
    return length 
            
def mostFrequentDigit(n):
    n = abs(n)
    length = countDigits(n) 
    occurences = 0 
    occurencesPrevNum= 0
    mostNum = 0 
    if n < 10:
        return n 
    for num in range(0, 10):
        occurences = 0 
        for digit in range(0,length):
            if num == getKthDigit(n,digit): 
                occurences += 1 
            if occurences > occurencesPrevNum: 
                occurencesPrevNum = occurences 
                mostNum = num
    return mostNum

def isPrime(n): 
    if n < 2: 
        return False 
    if n ==2: 
        return True
    if n % 2 == 0: 
        return False 
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor + 1,2): 
        if n % factor == 0: 
            return False 
    return True 

def getKthDigit(n, k):
    if n < 0:
        chopOffRightDigits = -n//10**k
    else: 
        chopOffRightDigits = n//10**k
    return chopOffRightDigits % 10 
    
def isPalindromic(n): 
    if n < 10: 
        return True
    length = 0 
    otherN = n 
    while(otherN > 0): 
        length += 1 
        otherN //= 10 
    compareN = n 
    middleSpot = roundHalfUp(length/2)
    #write a function that switches the numbers : 123 to 321 for example 
    res = 0 
    for i in range(0,length): 
        onesDigit = compareN % 10
        compareN //= 10
        res += onesDigit*(10**(length - i -1))
    if res == n :
       return True
    else:
        return False

def isPalindromicPrime(n):
    if (isPrime(n) and isPalindromic(n)): 
        return True
    return False

def nthPalindromicPrime(n):
    found = 0 
    guess = 0 
    while (found <= n): 
        guess += 1
        if(isPalindromicPrime(guess)):
            found += 1 
    return guess 

def carrylessAdd(x, y):
    # we need to do mod 10 so that the other number is  not carried# 
    #calculate lengthX and lengthY
    changeX = x
    changeY = y 
    lengthX = 0 
    lengthY = 0 
    while(changeX > 0):
        lengthX += 1 
        changeX //= 10 
    while(changeY > 0): 
        lengthY += 1 
        changeY //= 10 
    
    #now add the two numbers 
    add = 0 
    if lengthX > lengthY : 
        for i in range(0,lengthX):
            add += ((getKthDigit(x,i) + getKthDigit(y,i)) % 10) * 10**(i) 
    else:
        for i in range(0,lengthY): 
            add += ((getKthDigit(x,i) + getKthDigit(y,i)) % 10) * 10**(i) 
    return add 

def integral(f, a, b, N):
    width = (b-a)/N 
    x1 = a 
    x2 = a + width 
    area = 0 
    #area of a trapezoid = ((a+b)/2)*h 
    for x in range(0,N): 
        area += ((f(x1) + f(x2)) / 2)*(width)
        x1 += width 
        x2 += width 
    return area
def checkIsNumber(n,appears): 
    check = n 
    length = 0
    while(check > 0):
        length += 1
        check //= 10
    total = None
    for num in range(0,length): 
        if appears == getKthDigit(n,num): 
            total = True
    if(not total): 
        return False
    return total 

def isProperty309(n): 
    #create a function that checks if how many times a number appears in a num 
    #do for loop from 0 to 10 and if it returns true using that function
    #then you done
    for num in range(0,10):
        total = None 
        if checkIsNumber(int(math.pow(n,5)), num): 
            total = True 
        else : 
            return False 
    return total 
    
def nthWithProperty309(n):
    found = 0 
    guess = 0 
    while(found <= n): 
        guess += 1 
        if(isProperty309(guess)):
            found += 1 
    return guess

def isCircularPrime(n): 
 #for loop switches numbers to left?#
 # need to do a loop that switches it to the left 
    if not isPrime(n):
        return False

    compareN = 0 
    check = n 
    length = 0
    getDigit = 0 
    
    while(check >0): 
        length += 1 
        check //= 10
    
    for num in range(0,length):
        if(getKthDigit(n,num) == 0): 
            return False
    
    # switch the rightMost to the right and check that way only one for loop
    compareN = n  
    for num in range(0, length):
        rightMost = compareN % 10
        compareN //= 10 
        addLeft = (rightMost)*10**(length - 1)
        compareN += addLeft
        if(not isPrime(compareN)): 
            return False
    return True
         
def nthCircularPrime(n):
    found = 0 
    guess = 0 
    while(found <= n): 
        guess += 1
        if(isCircularPrime(guess)): 
            found +=1 
    return guess 

def calculateMiddleX(f, x0, y0, x1, y1, middleX, middleY,epsilon): 
    while(middleY > epsilon or middleY < -epsilon): 
        if((y0 > 0 and middleY > 0) or (y0 < 0 and middleY < 0)): #crasheshere
            x0 = middleX
            middleX = (x0 + x1) / 2
            middleY = f(middleX)
        elif((y1 > 0 and middleY > 0) or (y1 < 0 and middleY < 0)): 
            x1 = middleX
            middleX = (x1 + x0) / 2
            middleY = f(middleX) 
    return middleX    
def findZeroWithBisection(f, x0, x1, epsilon):
    y0 = f(x0)
    y1 = f(x1)
    middleX = (x0 + x1) / 2
    middleY = f(middleX)
    
    if (middleY == 0):
        return middleX

    return calculateMiddleX(f, x0 ,y0 ,x1 ,y1 ,middleX ,middleY, epsilon)
def nthSmithNumber(n):
    return 42

def carrylessMultiply(x1, x2):
    return 42

def calculateLength(n): 
    check = n
    length = 0 
    while(check > 0): 
        length += 1 
        check //= 10 
    return length 


def isKaprekarNumber(n): 
    # split it into all posible cases not just two equal length 
    square = int(math.pow(n,2))
    
    length = calculateLength(square)
    middleSpot = int(length/2)

    #num1 = splitNumber1stHalf(square, middleSpot)
    #num2 = splitNumber2ndHalf(square, middleSpot) 
    #
    if(num1 + num2 == n):
        return True
    return False
def nthKaprekarNumber(n): 
    found = 0 
    guess = 0 
    while(found <= n): 
        guess += 1 
        if(isKaprekarNumber(guess)):
            found += 1
    return guess

def nthCarolPrime(n):
    return 42

def play112(game):
    return 42
def amIsmart():
    return False

############################
# integerDataStructures
# If you do this spicy problem,
# place your solutions here!
############################

#################################################
# Test Functions
# ignore_rest (tell autograder to ignore everything below here)
#################################################

def testDrawFancyWheels():
    print('Testing drawFancyWheels()... (confirm visually)')
    print('  drawFancyWheels: 1 row x 1 col, win size of 400x400...', end='')
    basic_graphics.run(1, 1, width=400, height=400, drawFn=drawFancyWheels)
    print('  drawFancyWheels: 4 rows x 6 cols, win size of 900x600...', end='')
    basic_graphics.run(4, 6, width=900, height=600, drawFn=drawFancyWheels)

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(1) == 418)
    assert(nthWithProperty309(2) == 462)
    assert(nthWithProperty309(3) == 474)
    print("Passed!")

def testNthCircularPrime():
    print('Testing nthCircularPrime()...', end='')
    # [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113,
    #  131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, ...]
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(20) == 719)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testNthCarolPrime():
    print("Testing nthCarolPrime()...", end='')
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(2) == 223)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    assert(nthCarolPrime(8) == 68718952447)
    assert(nthCarolPrime(9) == 274876858367)
    print("Passed!")

def testPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length-encoded 0
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # [1, 42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # [1, 567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # [1, 9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # [1, 9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # [ 0 ]
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # [ 0 ]
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # [ 2, 42, 73 ]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # [ 2, 42, 98765 ]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # [ 4, 42, 98765, 99, 0 ]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # 6* -> 1
    fsm = setTransition(fsm, 1, 7, 2) # 7 -> 2
    fsm = setTransition(fsm, 2, 7, 2) # 7* -> 2
    fsm = setTransition(fsm, 2, 8, 3) # 7* -> 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # [1, 65]
    assert(encodeString('f') == 1111113102) # [1, 102]
    assert(encodeString('3') == 111111251) # [1, 51]
    assert(encodeString('!') == 111111233) # [1, 33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # [4,65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
    testEncodeDecodeStrings()

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # required
    testDrawFancyWheels()

    # mild
    testMostFrequentDigit()
    testNthPalindromicPrime()
    testCarrylessAdd()
    testIntegral()
    testNthWithProperty309()
    testNthCircularPrime()

    # medium
    testFindZeroWithBisection()
    #testNthSmithNumber()
    #testCarrylessMultiply()
    #testNthKaprekarNumber()
    #testNthCarolPrime()

    # spicy
    #testPlay112()
    #testIntegerDataStructures()

def main():
    cs112_s20_unit2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
