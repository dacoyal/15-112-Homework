#################################################
# hw9.py
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2
#
# Names and andrew id's of up to 3 collaborators:
#   name + andrew id #1:
#   name + andrew id #2:
#   name + andrew id #3:
#################################################

import cs112_s20_unit9_linter
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

#################################################
# Functions for you to write
#################################################

def alternatingSum(L, count = 0):
    #if the length of our list is 0 we just return 0
    if len(L) == 0:
        return 0
    else:
        #count will keep track of wether the track is positive or negative
        if count % 2 == 0:
            return L[0] - alternatingSum(L[1:])
        else:
            return L[0] + alternatingSum(L[1:])

def onlyEvenDigits(L, newL = None, count = 0):
    #count checks how many times we called onlyEven to make sure the list is
    #empty at the beginning
    if newL == None:
        newL = []

    if L == [] and count == 0:
        return L

    if len(L) == 0:
        return newL

    else:
        count += 1
        #we will call our helper fuction on every number to convert them into
        #numbers made of only even numbers
        newNumber = checkForEvens(L[0])
        newL.append(newNumber)
        return onlyEvenDigits(L[1:], newL, count)
#this function will modifiy the number to keep only the even digits of a number
def checkForEvens(number, newNumber = 0, powerOf10 = 1, depth = 1):
    #base case checks if we have already loooped through the whole number
    firstDigitFromRight = number % 10
    if number <= 0:
        return newNumber
    else:
        #first we get the number from the very left
        if firstDigitFromRight % 2 == 0:
            #add the firstDigit to our newNumber
            newNumber += firstDigitFromRight * powerOf10
            number //= 10
            #strip down the number by 10
            powerOf10 *= 10
            return checkForEvens(number, newNumber, powerOf10)
        else:
            number //= 10
            return checkForEvens(number, newNumber, powerOf10)

def powersOf3ToN(n, nextPower = 0, newL = None, depth = 0):
    #once our exponent is less than 1 we just return an empty list
    if newL == None:
        newL = []

    if nextPower == 0:
        newL.append(1)

    if n < 1:
        return []

    else:
        #every time we move on our power increments by 1
        nextPower += 1
        nextNumber = 3**nextPower
        #if next number is greater than our number then we stop looping
        if(nextNumber > n):
            return newL
        newL.append(nextNumber)
        return powersOf3ToN(n, nextPower, newL, depth + 1)

def binarySearchValues(L, item, newL = None, low = 0, high = 0):
    if newL == None:
        newL = []
        high = len(L) - 1
    
    if L[low:high+1] == []:
        return newL

    else:
        #our middle index will be the highest index plus the lowest index 
        #divided by 2. With that we can the mid letter
        midIndex = (high + low)//2
        midLetter = L[midIndex]
        #if the item equals the midletter we add the item to the list and return
        #our list
        if item == midLetter:
            newL.append( (L.index(item), item) )
            return newL
        #if the ASCII value of the midLetter is lower than the item we are
        #searching for then we have to increment our lower index by 1
        elif (midLetter) < (item):
            newL.append( (L.index(midLetter), midLetter) )
            low = midIndex + 1
            return(binarySearchValues(L, item, newL, low, high))
        #else if the ASCII value of the midletter is higher than the item we 
        #decrease the highest index by 1
        elif midLetter > item:
            newL.append( (L.index(midLetter), midLetter) )
            high = midIndex - 1
            return(binarySearchValues(L, item, newL, low, high))

def secondLargest(L, bestValue = None, secondBestValue = None, count = 0):
    #if our list is only one number return None
    if count == 0 and (len(L) == 1 or len(L) == 0):
        return None

    if L == []:
        return secondBestValue
    else:
        count += 1
        currentValue = L[0]
        #first set the best value equal to the first number in the list
        if bestValue == None and secondBestValue == None:
            bestValue = currentValue
        #this is executed the second time we loop through the list when
        #secondBestValue is None
        elif bestValue != None and secondBestValue == None:
            if currentValue < bestValue:
                secondBestValue = currentValue
                return secondLargest(L[1:], bestValue, secondBestValue, count)
            #if currentValue is equal to the bestValue we make it equal to
            #the secondBestValue
            elif currentValue == bestValue:
                secondBestValue = currentValue
                return secondLargest(L[1:], bestValue, secondBestValue, count)
            #if the currentValue is greater than bestValue then it becomes our
            #best value
            elif currentValue > bestValue:
                secondBestValue = bestValue
                bestValue = currentValue
                return secondLargest(L[1:], bestValue, secondBestValue, count)

            else:
                return secondLargest(L[1:], bestValue, secondBestValue, count)

        elif currentValue > bestValue:
            secondBestValue = bestValue
            bestValue = currentValue

        #if the next number of the list is smaller than the best value set the
        #second best value to that number
        elif currentValue > secondBestValue and currentValue < bestValue:
            secondBestValue = currentValue
        return secondLargest(L[1:], bestValue, secondBestValue, count)

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([1,3,3,4,5]) == 1-3+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

def testSecondLargest():
    print('Testing secondLargest()...', end='')
    assert(secondLargest([1,2,3,4,5]) == 4)
    assert(secondLargest([4,3]) == 3)
    assert(secondLargest([4,4,3]) == 4)
    assert(secondLargest([-3,-4]) == -4)
    assert(secondLargest([4]) == None)
    assert(secondLargest([ ]) == None)
    print('Passed!')

def testOnlyEvenDigits():
    print('Testing onlyEvenDigits()...', end='')
    assert(onlyEvenDigits([43, 23265, 17, 58344]) == [4, 226, 0, 844])
    assert(onlyEvenDigits([44, 23265, 17, 58344]) == [44, 226, 0, 844])
    assert(onlyEvenDigits([ ]) == [ ])
    print('Passed!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(10.5) == [1, 3, 9])
    assert(powersOf3ToN(27) == [1, 3, 9, 27])
    assert(powersOf3ToN(26.999) == [1, 3, 9])
    assert(powersOf3ToN(2186.5) == [1, 3, 9, 27, 81, 243, 729])
    assert(powersOf3ToN(-1) == [ ])
    print('Passed!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c') ==
           [(2, 'f'), (0, 'a'), (1, 'c')])
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'n') ==
           [(2, 'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 0) ==
    [(15,15), (7,7), (3,3), (1,1), (0,0)])
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    print()
    print('Testing **** non-spicy *** hw9 problems!')
    print()

    # mild+medium problems:
    testAlternatingSum()
    testOnlyEvenDigits()
    testPowersOf3ToN()
    testBinarySearchValues()
    testSecondLargest()

    # spicy problems:  NOT HERE!!!
    pass

def main():
    cs112_s20_unit9_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
