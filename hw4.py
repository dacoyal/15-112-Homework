#################################################
# hw4.py
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2
#################################################

import cs112_s20_unit4_linter
import basic_graphics
import string, copy, random, math

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

#################################################
# Person class
#################################################

class Person(object):
    def __init__(self, name, age): 
        self.name = name
        self.age = age 
        self.friends = []

    def getName(self):
        return self.name

    def getAge(self): 
        return self.age
    
    def addFriend(self, other): 
        if other not in self.friends:
            self.friends.append(other)
        if self not in other.friends:
            other.friends.append(self)
    
    def addFriends(self, other):  
        for friend in other.friends: 
            self.addFriend(friend)
    
    def getFriends(self): 
        return self.friends 
    
    def getFriendsNames(self): 
        ans = []
        for friend in self.friends: 
            ans.append(friend.name)
        return sorted(ans)
    
#################################################
# removeEvens
#################################################

def destructiveRemoveEvens(L):
    i = 0
    while(i < len(L)): 
        if L[i] % 2 == 0 :
            L.remove(L[i])
        else: 
            i += 1 
    return L

def nondestructiveRemoveEvens(L):
    ans = [ ]
    for i in range(len(L)): 
        if L[i] % 2 != 0 : 
            ans.append(L[i])
    return ans 

#################################################
# bestScrabbleScore
#################################################
#function loops through a word and adds up all the scores of its individial
#'abc'.count('a')
def canMakeWord(word, hand):
    listHand = list(hand)
    for i in range(len(word)): 
        if word[i] in listHand:
            listHand.remove(word[i])
        else: 
            return False
    return True

def getScore(word, letterScores): 
    score = 0 
    for i in word:  
        score += letterScores[ord(i) - ord("a")]
    return score 

def bestScrabbleScore(dictionary, letterScores, hand): 
# function of can i make this word?  
# if yes, calculate best score
    make = None
    bestScore = 0 
    bestWord = ''
    bestWordList =[]
    for word in dictionary: 
        currentWord = word 
        if canMakeWord(word, hand):
            score = getScore(word, letterScores)
            if score == bestScore: 
                bestWordList.append(word)
            if score > bestScore: 
                bestScore = score 
                bestWordList.append(currentWord)
    for c in bestWordList: 
        bestWord += c
    if bestWordList == []:
        return None 
    if len(bestWordList) > 1: 
        return (bestWordList, bestScore)
    return (bestWord, bestScore)
#################################################
# solvesCryptarithm
#################################################
def solvesCryptarithm(puzzle, solution):
    score = 0 
    currentNumber = ""
    firstScore = 0 
    puzzle = puzzle.split(" ")
    firstName = puzzle[0]
    #loops through the first word
    for i in firstName: 
        if i not in solution: 
            return False 
        currentNumber += str(solution.find(i))
    firstScore = int(currentNumber)
    secondName = puzzle[2]
    currentNumber = ""
    #loops through the second word
    for x in secondName: 
        if x not in solution: 
            return False
        currentNumber += str(solution.find(x))
    secondScore = int(currentNumber)
    solutionScore = ""
    #loop through the third word
    for j in puzzle[4]: 
        if j not in solution: 
            return False
        solutionScore += str(solution.find(j))
    return (firstScore + secondScore == int(solutionScore))
    
#################################################
# drawLetterTypePieChart(canvas)
#################################################

#this function eliminates white spaces from the text
def eliminateWhiteSpaces(text) :
    ans = ""
    for i in range(len(text)): 
        if not text[i].isspace():
            ans += text[i]
    return ans
#gets the count of consonants, vowels and other
def getCount(text): 
    numVocals = 0 
    numConsonants = 0 
    numOther = 0 
    checkConsonant = 'bcdfghjklmnopqrstvwxyz'
    checkVowel = 'aeiou'
    if len(text) == 0: 
        return 0,0,0
    for i in range(len(text)):  
        if text[i] in checkVowel or text[i] in checkVowel.upper(): 
            numVocals += 1 
        elif text[i] in checkConsonant or text[i] in checkConsonant.upper(): 
            numConsonants += 1 
        else: 
            numOther += 1 
    return numVocals, numConsonants, numOther
#gets the percentage of consonants, vowels and other
def getPercentages(text): 
    numVocals = 0 
    numConsonants = 0 
    numOther = 0 
    checkConsonant = 'bcdfghjklmnopqrstvwxyz'
    checkVowel = 'aeiou'
    if len(text) == 0: 
        return 0,0,0
    for i in range(len(text)):  
        if text[i] in checkVowel or text[i] in checkVowel.upper(): 
            numVocals += 1 
        elif text[i] in checkConsonant or text[i] in checkConsonant.upper(): 
            numConsonants += 1 
        else: 
            numOther += 1 
    return (numConsonants/len(text), numVocals/len(text),numOther/len(text))

def drawPieWedge(canvas, r, cx, cy, startAngle, percentage, color):
    startX = cx - r 
    startY = cy + r 
    angle = (360 * percentage) 
    endX = cx + r + 20 
    endY = cy  - r 
    typeLetter = ""
    if percentage == 0: 
        return startAngle + angle
    if percentage == 1 : 
        canvas.create_oval(startX, startY, endX, endY, fill = color)
    else:
        canvas.create_arc(startX, startY,endX, endY, start = startAngle ,
        extent = angle, fill = color)
    return startAngle + angle
def setColor(color): 
    typeLetter = ""
    if color == "pink": 
        typeLetter += "vowels"
    elif color == "cyan": 
        typeLetter += "consonants"
    elif color == "lightGreen" :
        typeLetter += "other"
    return typeLetter
#creates the text 
def createText(canvas,color, count, startAngle, endAngle, lengthText, cx, cy,
    percentage,text ,r): 
    total = True
    typeLetter = setColor(color)
    middleAngle = (endAngle - startAngle) / 2
    x1 = r/2*math.cos(math.radians(middleAngle + startAngle))
    y1 = r/2*math.sin(math.radians(middleAngle + startAngle))
    exit = False
    if len(text) == 0 : 
        total = False
    if total == False: 
        canvas.create_text(cx, cy,
        font = ("Arial 14 bold"),  
        text = f'No data to display')
    elif percentage == 1 and percentage != 0: 
        canvas.create_text(cx, cy, font = "Arial 12 bold",
        text = f'{typeLetter}({count} of {lengthText},' +
        f'{roundHalfUp(percentage*100)}%)')
        exit = True
    elif exit != True and percentage != 0:
        canvas.create_text(x1 + cx, -y1 + cy ,
        font = ("Arial 12 bold"),  
        text = f'{typeLetter}({count} of {lengthText},' +
        f'{roundHalfUp(percentage*100)}%)') 

def drawLetterTypePieChart(canvas, text, cx, cy, r):
    newText = eliminateWhiteSpaces(text)
    lengthText = len(newText)
    x1Text = len(newText) - cx
    y1Text = cy + r + 10
    consonants, vocals, other = getPercentages(newText)
    startAngle = 90
    countVocals, countConsonants, countOther = getCount(text)
    #draws pie of vocals
    startAngle1 = drawPieWedge(canvas, r, cx, cy, startAngle,
    vocals, color = 'pink')
    color1 = 'pink'
    createText(canvas, color1, countVocals, startAngle, startAngle1, lengthText,
    cx, cy, vocals, newText, r)
    #draws pie of consonants
    startAngle2 = drawPieWedge(canvas, r, cx, cy, startAngle1,
    consonants, color = 'cyan')
    color2 = 'cyan'
    createText(canvas,color2, countConsonants, startAngle1, startAngle2,
    lengthText, cx, cy, consonants, newText, r)
    #draws pie of other
    startAngle3 = drawPieWedge(canvas, r, cx, cy, startAngle2,
    other, color = 'lightGreen')
    color3 = 'lightGreen'
    createText(canvas, color3, countOther, startAngle2, startAngle3, lengthText,
    cx, cy, other, newText, r)
    canvas.create_text(cx + 10 , cy - r - 20, font = "Arial 18 bold", 
    text = f''' Text: '{text}' ''') 

