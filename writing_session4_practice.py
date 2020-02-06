#################################################
# writing_session4_practice_solutions.py
#################################################

import cs112_s20_unit4_linter
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
import copy
'''
def ct():
    # fill in each space to the right of each print statement
    # with the value it prints

    print([3,2,1] > [3,2])  # True       

    a = [1]                         
    b = a   
    c = copy.copy(a)  
    a += [2] 
    a = a + [3]
    print(a, b, c)                       # [1, 2, 3] [1, 2] [1]

    a = [2,3,5,3,2]
    a.remove(2)
    v = a.pop(2)
    print(a, v)                          # [3, 5, 2] 3

    L = list(range(1,7,2))
    M = [v**2 for v in L]
    N = [v*10 for v in M if v < 10]
    print(L, M, N)                      # [1, 3, 5] [1, 9, 25] [10, 90]

    L = ['A', 'BC', 'D']
    print('xy'.join(L))                 # AxyBCxyD

ct()'''

'''/ 
1. Which of these does not set M to a copy of L?
    a) M = copy.copy(L) 
    b) M = L[:]
    c) M = L + [ ]
--> d) M = L 
    e) M = list(L)

2. If a function f(L) does not return a value (so technically it returns None),
   which is more likely:
-->a) f(L) is destructive
   b) f(L) is non-destructive

3. Assuming L is a list and s is a string, which of the following methods
   does not exist:
   a) L.index(v)
-->b) L.find(v)
   c) s.index(c)
   d) s.find(c)

4. What is the difference between L.append(v) and L.extend(v)?
   a) There is no difference 
-->b) L.append adds one value and L.extend adds a list of values
   c) L.append adds to the end of L and L.extends adds to the start of L
   d) There is no such thing as L.extend

5. Fill in the blank so that M is equal to L, only with the value 5
   nondestructively inserted at index 3 (so L is unchanged). 
   You may assume len(L)>3: 

   M = copy.copy(L.insert(3,5))

6. Which kind of loop should we use if we are adding and/or removing values
   from a list L while looping over it?
   a) for v in L
-->b) while i < len(L)

7. What is the difference between L.sort() and sorted(L)?
   a) L.sort() is faster than sorted(L)
-->b) L.sort() is destructive and sorted(L) is non-destructive
   c) L.sort() is non-desructive and sorted(L) is destructive
   d) Nothing -- they do the same thing.

8. What is the key difference between a tuple and a list?
-->a) Tuples can only contain exactly 2 values, lists can contain any number of
    values
   b) Tuples are mutable, lists are not
   c) Tuples are immutable, lists are not
   d) Tuples can only contain numbers, lists can contain any type of value

9. Fill in the blank so that T refers to a singleton (length 1) tuple
   containing just the value 42:

   T = (42,)

10. Fill in the blank with a list comprehension so that M contains the
    list of the squares of the values in L, which you may assume is a list
    of integers:

    M = [i**2 for i in L]
/'''
def alternatingSum(L): 
    return sum(L[0::2]) - sum(L[1::2])

def median(L):
    n = len(L)
    L = sorted(L)
    if(L == [ ]): return None 
    if len(L) % 2 == 0 : #if even length
        return (L[n//2] + L[(n//2) - 1])/2
    else: #if odd length 
        return L[n//2]

def isSorted(L):
    if len(L) == 0 : 
        return True
    currentDigit = 0
    previousDigit = L[0] 
    for i in range(len(L)):
        currentDigit = L[i]
        if i < (len(L) - 1) and i > 0:
            if currentDigit < previousDigit and currentDigit < L[i+1]: 
                return False 
            elif currentDigit > previousDigit and currentDigit > L[i+1]: 
                return False
        previousDigit = L[i]
    return True

def smallestDifference(L):
    if len(L) == 1: 
        return L[0]
    if len(L) == 0 : 
        return -1 
    currentDigit = L[0]
    smallestDiff = None
    nextDigit = L[0]
    currentDiff = 0 
    for i in range(len(L)): 
        for x in range(i+1,len(L)):
            currentDigit = L[i]
            nextDigit = L[x]
            currentDiff = abs(currentDigit - nextDigit)
            if smallestDiff == None : 
                smallestDiff = currentDiff
            
            if currentDiff < smallestDiff : 
                smallestDiff = currentDiff
    return smallestDiff

def lookAndSay(L):
    if L == []: 
        return L
    runCount = 1
    result = [ ]
    runDigit = L[0] 
    for current in L[1:]:
        if current == runDigit: 
            runCount +=1 
        else:
            result += [(runCount, runDigit)]
            runCount = 1 
            runDigit = current 
    return result + [(runCount,runDigit)]

def inverseLookAndSay(L):
    ans = [ ]
    multiply = 0
    number = 0 
    for i in range(len(L)):
        multiply = (L[i])[0] 
        number = (L[i])[1]
        for c in range(multiply):
            ans.append(number)
    return ans


def nondestructiveRemoveRepeats(L):
    newList = [ ]
    for num in L: 
        if num not in newList:
            newList.append(num)
    return newList
def destructiveRemoveRepeats(L):
    i = 0
    while(i < len(L)): 
        elem = L[i]
        if elem in L[:i]: 
            L.pop(i)
        else: 
            i += 1

class VoteTally(object):
    def __init__(self, candidates): 
        self.candidates = candidates
        self.counts = [0]*len(candidates)
    
    def addVotes(self, count, candidate): 
        if candidate not in self.candidates: 
            return f'No such candidate as {candidate}'
        if candidate == 'Total': 
            return sum(self.counts)
        i = self.candidates.index(candidate)
        self.counts[i] += count
        return self.counts
    
    def getVotes(self,candidate): 
        if(candidate == 'Total'): 
            return sum(self.counts)
        if candidate not in self.candidates: 
            return f'No such candidate as {candidate}'
        i = self.candidates.index(candidate)
        return self.counts[i]
    
    def addVoteTally(self,other):
        newCandidates = copy.copy(self.candidates)
        for candidate in other.candidates:
            if candidate not in newCandidates:
                newCandidates.append(candidate)
        newVT = VoteTally(newCandidates)
        for candidate in newCandidates: 
            if candidate in self.candidates: 
                newVT.addVotes(self.getVotes(candidate),candidate)
            if candidate in other.candidates: 
                newVT.addVotes(other.getVotes(candidate),candidate)
        return newVT
        
#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed.')

def testMedian():
    print('Testing median()...', end='')
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed')

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

def testVoteTallyClass():
    print('Testing VoteTally class...', end='')

    # When we create a VoteTally, we provide a list of
    # candidates whose votes we are tallying:
    vt1 = VoteTally(['Fred', 'Wilma', 'Betty'])

    # We can then add votes for the candidates
    vt1.addVotes(5, 'Fred')
    vt1.addVotes(3, 'Wilma')
    vt1.addVotes(2, 'Fred')

    # If we add votes to a non-candidate, we do so gracefully:
    assert(vt1.addVotes(3, 'Bam-Bam') == 'No such candidate as Bam-Bam')

    # And we can get the total tally of votes for each candidate
    assert(vt1.getVotes('Fred') == 7)
    assert(vt1.getVotes('Wilma') == 3)
    assert(vt1.getVotes('Betty') == 0)

    # And we can gracefully handle non-candidates
    assert(vt1.getVotes('Barney') == 'No such candidate as Barney')

    # And we can also get the overall total
    assert(vt1.getVotes('Total') == 10)

    # Here is a second VoteTally with some (but not all) of the same candidates
    vt2 = VoteTally(['Fred', 'Barney', 'Betty']) 
    vt2.addVotes(5, 'Fred')
    vt2.addVotes(2, 'Betty')
    vt2.addVotes(8, 'Betty')
    assert(vt2.getVotes('Fred') == 5)
    assert(vt2.getVotes('Wilma') == 'No such candidate as Wilma')
    assert(vt2.getVotes('Betty') == 10)
    assert(vt2.getVotes('Barney') == 0)
    assert(vt2.getVotes('Total') == 15)

    # We can combine two VoteTally objects to create a third
    # VoteTally object, which includes all the candidates from either
    # tally, and combines their totals:
    vt3 = vt1.addVoteTally(vt2)
    assert(vt1.candidates == ['Fred', 'Wilma', 'Betty']) # unchanged
    assert(vt2.candidates == ['Fred', 'Barney', 'Betty']) # ditto
    # but the new VoteTally is created with a sorted list of candidates
    # in the same order as they appear first in vt1 then vt2,
    # but with no duplicates
    assert(vt3.candidates == ['Fred', 'Wilma', 'Betty', 'Barney'])
    assert(vt3.getVotes('Fred') == 12)
    assert(vt3.getVotes('Wilma') == 3)
    assert(vt3.getVotes('Betty') == 10)
    assert(vt3.getVotes('Barney') == 0)
    assert(vt3.getVotes('Pebbles') == 'No such candidate as Pebbles')
    assert(vt3.getVotes('Total') == 25)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()
    testMedian()
    testIsSorted()
    testSmallestDifference()
    testLookAndSay()
    testInverseLookAndSay()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    testVoteTallyClass()

def main():
    cs112_s20_unit4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
