#################################################
# hw3.py
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2
#################################################

import cs112_s20_unit3_linter
#import basic_graphics
import string, copy, random

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

#this function returns the player with the best score
def getBestPlayer(data): 
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bestScore = 0
    bestName = ''
    #loops through each line formed by split lines 
    for line in data.splitlines(): 
        tempScore = 0 
        tempName = ''
        #loops through every character that is not a comma 
        for c in line.split(','): 
            #we will keep track of our temporary name and score 
            #we also need a best score and name to keep track of the best player
            if c[0] in alphabet or c[0] in alphabet.lower():
                tempName = c 
            else: 
                tempScore += int(c)
                if tempScore > bestScore: 
                    bestScore = tempScore 
                    bestName = tempName 
                elif tempScore == bestScore: 
                    if tempName not in bestName:
                        bestName += "," + tempName
    return bestName

def topScorer(data):
    if(data == ''): 
        return None
    return getBestPlayer(data)
#this function converts all the spaces in the string into hyphons
def convertHyphon(str1): 
    finalAns = ''
    for i in range(len(str1)):
        if str1[i] == ' ': 
            finalAns += '-'
        else:
            finalAns += str1[i]
    return finalAns
#this function splits a string into different lines
def splitIntoLines(text,width):
    str1 = ''
    for i in range(0, len(text)):
        if (i % width == 0):
            str1 += "\n" + text[i]    
        else: 
            str1 += text[i]
        #string1 contains our answer without hyphons and without the spaces 
        #removed 
    return str1[1:]
#this function will remove the spaces in the string at the beginning and end
# of a line
def removeSpaces(str1,width):   
    ans = ''
    startIndex = 0 
    endIndex = 0 
    leave = False
    #our leave variable is to make sure when we know when we need to stop to
    # check for spaces
    for line in str1.splitlines():
        startIndex = 0 
        endIndex = len(line) - 1
        leave = False
        while not leave: 
            if line[startIndex] == ' ': 
                startIndex += 1
            elif line[endIndex] == ' ': 
                endIndex -= 1 
            elif line[startIndex] != ' ' and line[endIndex] != ' ': 
                leave = True 
                ans += '\n' + line[startIndex:endIndex+1]
    return ans[1:]

def wordWrap(text, width):
    # Hint: this is probably easier without using text.splitlines()\
    
    if width >= len(text):
        return text
    str1 = splitIntoLines(text,width)
    #string1 contains our answer without hyphons and without the spaces 
    #removed 
    str1NoSpace = removeSpaces(str1,width)
    final = convertHyphon(str1NoSpace)
    return final

#isPalindrome was used from lecture notes: strings section 
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#isPalindrome
def isPalindrome(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]):
            return False
    return True
#this function checks for the longest and greatest ASCII. It keeps on checking
#all the possible strings and gets the longest and best Palindrome
def longestSubpalindrome(s): 
    bestPalindrome = ''
    currentPalindrome = ''
    for i in range(len(s)):
        for x in range(i,len(s)):
            xInclusive = x + 1
            if isPalindrome(s[i:xInclusive]): 
                currentPalindrome = s[i:xInclusive]
            if len(currentPalindrome) > len(bestPalindrome) : 
                bestPalindrome = currentPalindrome 
            elif (len(currentPalindrome) == len(bestPalindrome) and 
                currentPalindrome > bestPalindrome):
                 bestPalindrome = currentPalindrome
    return bestPalindrome   

#this function gets the amount of exact matches that occur
def exactScore1(target,guess):
    exactCount = 0 
    for i in range(len(target)): 
        for x in range(len(guess)):
            if target[i] == guess[x] and i == x:
                exactCount += 1
    return exactCount 
#this function gets the amount of partial matches that occur
def partialScore(target,guess): 
    score = 0
    for i in range(len(target)): 
        for x in range(len(guess)):
            #if you find an exact match then break
            if target[i] == guess[x] and i == x:
                break
            if target[i] == guess[x] and i != x:
                score += 1
                break      
    return score 
#this function returns the correct message depending on the partial and exact
#scores
def returnMessage(partialScore1,exactScore):
    if partialScore1 ==0 and exactScore == 0:
        return "No matches"
    elif exactScore == 0 and partialScore1 > 1: 
        return str(partialScore1) + " partial matches"
    elif exactScore == 0 and partialScore1 == 1: 
        return str(partialScore1) + " partial match"  
    elif partialScore1 == 0 and exactScore > 1:
        return  str(exactScore) + " exact matches"
    elif partialScore1 == 0 and exactScore == 1:
        return str(exactScore) + " exact match"
    elif exactScore == 1 and partialScore1 > 1 : 
        return (str(exactScore) + " exact match, " + str(partialScore1) 
        + ' partial matches')
    elif exactScore == 1 and partialScore1 == 1: 
        return (str(exactScore) + " exact match, " + str(partialScore1) 
        + ' partial match')
    elif exactScore > 1 and partialScore1 == 1: #REFER
        return (str(exactScore) +' exact matches, '+ str(partialScore1) 
        + ' partial match')
    elif partialScore1 > 1 and exactScore == 1: 
        return (str(partialScore1) + " partial matches, " + str(exactScore)  
        + " exact match")
    elif partialScore1 > 1 and exactScore > 1: 
        return  (str(exactScore) + " exact matches, " + str(partialScore1) 
        + " partial matches")

def mastermindScore(target, guess):
    if target == guess:
        return("You win!!!")
    exactScore = exactScore1(target,guess)
    partialScore1 = partialScore(target,guess)
    return returnMessage(partialScore1, exactScore)

#################################################
# Test Functions
#################################################

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    data = '''\
Betty,0,0,0,0
Pebbles,0,0,0,0,123,0
Fred,11,20,30
Wilma,10,20,30,1
Barney,123
BamBam,120,1,1,0,1
''' 
    assert(topScorer(data) == 'Pebbles,Barney,BamBam')
    print('Passed!')

def testWordWrap():
    print('Testing wordWrap()...', end='')
    assert(wordWrap("abc", 3) == "abc")
    assert(wordWrap("abc",2) == "ab\nc") 
    assert(wordWrap("abcdefghij", 4)  ==  """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg",  4)  ==  """\
a-b
c-de
fg""")
    assert(wordWrap('a b c def  g h  ', 4) =="""\
a-b
c-de
f--g
h""")
    print('Passed!')

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    assert(longestSubpalindrome('abba') == 'abba')

    print("Passed!")

def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert(mastermindScore('abcd', 'aabd') ==
                           '2 exact matches, 1 partial match')
    assert(mastermindScore('efgh', 'abef') ==
                           '2 partial matches')
    assert(mastermindScore('efgh', 'efef') ==
                           '2 exact matches')
    assert(mastermindScore('ijkl', 'mnop') ==
                           'No matches')
    assert(mastermindScore('cdef', 'cccc') ==
                           '1 exact match')
    assert(mastermindScore('cdef', 'bccc') ==
                           '1 partial match')
    assert(mastermindScore('wxyz', 'wwwx') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('wxyz', 'wxya') ==
                           '3 exact matches')
    assert(mastermindScore('wxyz', 'awxy') ==
                           '3 partial matches')
    assert(mastermindScore('wxyz', 'wxyz') ==
                           'You win!!!')
    print("Passed!'")

def testPlayPoker():
    print('Testing playPoker()...', end='')
    assert(playPoker('QD-3S', 1) == 'Player 1 wins with a high card of QD')
    assert(playPoker('QD-QC', 1) == 'Player 1 wins with a pair to QD')
    assert(playPoker('QD-JS', 1) == 'Player 1 wins with a straight to QD')
    assert(playPoker('TD-QD', 1) == 'Player 1 wins with a flush to QD')
    assert(playPoker('QD-JD', 1) == 'Player 1 wins with a straight flush to QD')
    assert(playPoker('QD-JD', 2) == 'Not enough cards')

    assert(playPoker('AS-2H-3C-4D', 2) ==
                                    'Player 2 wins with a high card of 4D')
    assert(playPoker('5S-2H-3C-4D', 2) ==
                                    'Player 1 wins with a high card of 5S')
    assert(playPoker('AS-2H-3C-2D', 2) == 'Player 2 wins with a pair to 2H')
    assert(playPoker('3S-2H-3C-2D', 2) == 'Player 1 wins with a pair to 3S')
    assert(playPoker('AS-2H-2C-2D', 2) == 'Player 1 wins with a straight to 2C')
    assert(playPoker('AS-2H-2C-3D', 2) == 'Player 2 wins with a straight to 3D')
    assert(playPoker('AS-2H-4S-3D', 2) == 'Player 1 wins with a flush to 4S')
    assert(playPoker('AS-2H-4S-3H', 2) ==
                                    'Player 2 wins with a straight flush to 3H')
    assert(playPoker('2S-2H-3S-3H', 2) ==
                                    'Player 1 wins with a straight flush to 3S')

    assert(playPoker('AS-2D-3C-4C-5H-6D-7S-8D', 2) ==
                                    'Player 2 wins with a high card of 4C')
    assert(playPoker('AS-2D-3S-4C-5H-6D-7S-8D', 4) ==
                                    'Player 3 wins with a flush to 7S')
    print('Passed!')

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

def testFunDecoder(encodeFn, decodeFn):
    s1 = ''
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(' \n\n') + random.choice(string.digits)
    for s in ['a', 'abc', s1]:
        if (decodeFn(encodeFn(s)) != s):
            raise Exception(f'Error in {decodeFn.__name__} on {repr(s)}')
    return True

def testFunDecoders():
    print('Testing funDecoders()...', end='')
    testFunDecoder(bonusEncode1, funDecode1)
    testFunDecoder(bonusEncode2, funDecode2)
    testFunDecoder(bonusEncode3, funDecode3)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # required
    testTopScorer()

    # mild
    testWordWrap()
    testLongestSubpalindrome()

    # medium
    testMastermindScore()
    #testPlayPoker()

    # spicy
    #testEncodeAndDecodeRightLeftRouteCipher()
    #testTopLevelFunctionNames()
    #testGetEvalSteps()
    #testFunDecoders()

def main():
    cs112_s20_unit3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
