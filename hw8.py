#################################################
# hw8.py
#
# Your name: Alejandro Ruiz
# Your andrew id: aruiz2
#
# Names and andrew id's of up to 3 collaborators:
#   name + andrew id #1:
#   name + andrew id #2:
#   name + andrew id #3:
#################################################

import cs112_s20_unit8_linter
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

# from: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

#################################################
# Functions for you to write
#################################################

def movieAwards(oscarResults):
    result = {}
    for award, movie in oscarResults:
        #we want to count how many times a movie appears in the awards dict
        count = result.get(movie, 0) + 1
        result[movie] = count
    return result

def friendsOfFriends(friends):
    #create empty dictionary to which we will add things
    result = dict()
    for person in friends:
        #create empty sets to where we will add our values
        result[person] = set()
        for friend in friends[person]:
            for friendsOfFriends in friends[friend]:
                #check if the friendsofriends is not equal to ourself and that
                #friendsoffriends is also not a friend of ours
                if(friendsOfFriends != person and friendsOfFriends
                not in friends[person]):
                    result[person].add(friendsOfFriends)
    return result

def invertDictionary(d):
    invertDict = dict()
    for key in d:#loop through our previous dictionary
        if d[key] not in invertDict:
            #create a dictionary of values equal to our keys  
            invertDict[d[key]] = {key}
        else:
            invertDict[d[key]].add(key)
    return invertDict

def readDogDataCsvFileInto2dList(year):
    #create a variable containing the file name
    fileName = 'dog-licenses-2018-abridged.csv'
    #convert the year to str if it is not already
    if not isinstance(year, str):
        year = str(year)
    file1 = readFile(fileName)
    fileList =[]
    #convert our file variable to a list separated by the different lines
    for line in file1.splitlines():
        #make the lineList empty everytime we enter a new line
        lineList =[]
        #every line is made of a list containing each individual word separated
        for word in line.split(","):
            lineList.append(word)
        fileList.append(lineList)
    return fileList

def convert2dListToTable(data):
    table = []
    #loop through every line in our data and create an empty dictionary in each
    #line and add it to our table list
    for line in data:
        lineDict = dict()
        for col in range(len(line)):
            #every key is the element in the first row at a specific column
            key = data[0][col]
            lineDict[key] = line[col]
        table.append(lineDict)
    return table

#helper function for cleanData and it cleans the 0th column
def clean0thCol(table, key, line):
    valueZerothCol = (line[key].split(" "))
    allowedWords = {'Male', 'Female'}
    #if the word is not allowed then we pop it aka remove it
    ansStr = ''
    for word in valueZerothCol:
        if word in allowedWords:
            ansStr += word
        #once we have the right value we need to conver the list back
        #to a string.
    if ansStr == '':
        ansStr = 'Unknown'
    line[key] = ansStr
#this is a helper function that will clean the data for our second column
def cleanSecondColumn(table, key, line):
    #we need to separate the color into a list to separate if /
    value = line[key].lower().split("/")
    #if the lenght of our list is greather than 1 we know that there
    #is more than 1 color so...
    finalColorList = value
    if len(value) > 1:
        finalColorList = []
        for word in value:
            finalColorList.append(word)
    #append every word to the final list
    value = finalColorList
    line[key] = value
#this is a helper function that will clean the data for the dog column
def cleanDogData(table, key, line):
    value = line[key].title()
    ans = ''
    #make sure the value is all alphanumeric or spaces ONLY
    for letter in value:
        if letter.isalnum() or letter.isspace(): 
            ans += letter
    line[key] = ans

def cleanValidDateData(table, line, key):
    #loop through the word until we find a dash
    validDateStr = ''
    for letter in line[key]:
        if letter == "-": break
        validDateStr += letter
    line[key] = int(validDateStr)

def cleanData(table):
    #loop through every line in table to modify it
    for line in table[1:]:
        for key in line:
            #if we are in the first column we want to check that the value only
            #contains male female or unknown
            if key == 'LicenseType':
                clean0thCol(table, key, line)

            elif key == 'Breed' or key == 'Dog' or key == 'DogName':
                cleanDogData(table, key, line)

            elif key == 'Color':
                cleanSecondColumn(table, key, line)
            
            elif key == 'ExpYear':
                line[key] = int(line[key])
            
            elif key == 'ValidDate':
                cleanValidDateData(table, line, key)
                         
    return table

def getCleanedTable(year):
    #call all of the 3 previous functions we have written to do all the work
    listCsv = readDogDataCsvFileInto2dList(year)
    table = convert2dListToTable(listCsv)
    cleanedTable = cleanData(table)
    return cleanedTable

def getValueSets(year):
    table = getCleanedTable(year)
    ans = dict()
    #loop through the first line to get our keys and make empty sets
    for line in table[:1]:
        for element in line:
            ans[element] = set()
    #we need to loop through every row and colum of our previous table
    for row in table[1:]:
        for col in row:
            if (isinstance(row[col], list)): #loop trough the list and add the
                                             #colors to our set
                for word in row[col]:
                    ans[col].add(word)
            else:
                #if it is not a list we can simply just add it
                ans[col].add(row[col])
    return ans

def getValueCounts(year):
    loopTable = getCleanedTable(year)
    finalTable = dict()
    #first create the dictionaries inside our final table
    for line in loopTable[:1]:
        for element in line:
            finalTable[element] = dict()
    #loop through the loopTable and count
    for line in loopTable[1:]:
        for col in line: #col would give us Dog, Breed, ExpDate, etc
            #if it is not in the format of a list then get the count
            currentValue = line[col]
            if not isinstance(currentValue, list):
                finalTable[col][currentValue] = \
                finalTable[col].get(currentValue, 0) + 1
            else:
                #we loop through every word of the list
                for word in currentValue:
                    finalTable[col][word] = \
                    finalTable[col].get(word, 0) + 1
    return finalTable
    
def getMostPopularValues(year):
    tableValues = getValueCounts(year)
    finalTable = dict()
    #initialize our final dicitonary with the keys required
    #get the max values of each typy
    for key in tableValues:
        finalTable[key] = dict()
    #now our dictionary is initialized so we can add the max values
    for key in tableValues: #key would be breed, color, dogName,etc
        bestValue = 0
        bestElem = None
        bestElemSet = set()
        for element in tableValues[key]:
            currentValue = tableValues[key][element]
            prevElem = element
            
            #we need to check if it is equal to the best score too
            if currentValue == bestValue:
                bestElemSet.add(element)

            #check for the best value and if there is a new better one then we 
            #need to save the best element
            elif currentValue > bestValue:
                bestElem = element
                bestValue = currentValue
                bestElemSet = set([element])
        #check if our set has a length of more than 1
        if len(bestElemSet) > 1:
            finalTable[key] = bestElemSet
        else:
            finalTable[key] = bestElem

    return finalTable

def someMoreDataAnalysisCode(year): #do the same as max valeus and check that
    #the element is not the same as the best element, and then second best...
    tableValues = getValueCounts(year)
    finalTable = dict()
    #initialize our final dicitonary with the keys required
    #get the max values of each typy
    for key in tableValues:
        finalTable[key] = dict()
    #now our dictionary is initialized so we can add the max values
    for key in tableValues: #key would be breed, color, dogName,etc
        bestValue = 0
        secondBestValue = -1
        thirdBestValue = -2
        bestElem = None
        secondBestElem = None
        thirdBestElem = None
        bestElemSet = set()
        for element in tableValues[key]:
            if element != "Bella" and element != "Buddy":
                currentValue = tableValues[key][element]
                prevElem = element
            
            #we need to check if it is equal to the best score too
                if currentValue == bestValue:
                    bestElemSet.add(element)
            
            #check for the best value and if there is a new better one then we 
            #need to save the best element
                elif currentValue > bestValue:
                    bestElem = element
                    bestValue = currentValue
                    bestElemSet = set([element])
        #check if our set has a length of more than 1
        if len(bestElemSet) > 1:
            finalTable[key] = bestElemSet
        else:
            finalTable[key] = bestElem
    return finalTable

def someMoreDataAnalysis():
    return '''
Q1: What is the most popular zip code in the full 2018 data?
A1: 15108

Q2: What is the most popular dog name in the full 2018 data?
A2: Bella

Q3: What is the second-most-popular dog name in the full 2018 data?
A3: Buddy

Q4: What is the third-most-popular dog name in the full 2018 data?
A4: Max
'''

#################################################
# Test Functions
#################################################

def testMovieAwards():
    print('Testing movieAwards()...', end='')
    tests = [
      (({ ("Best Picture", "The Shape of Water"), 
          ("Best Actor", "Darkest Hour"),
          ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
          ("Best Director", "The Shape of Water") },),
        { "Darkest Hour" : 1,
          "Three Billboards Outside Ebbing, Missouri" : 1,
          "The Shape of Water" : 2 }),
      (({ ("Best Picture", "Moonlight"),
          ("Best Director", "La La Land"),
          ("Best Actor", "Manchester by the Sea"),
          ("Best Actress", "La La Land") },),
        { "Moonlight" : 1,
          "La La Land" : 2,
          "Manchester by the Sea" : 1 }),
      (({ ("Best Picture", "12 Years a Slave"),
          ("Best Director", "Gravity"),
          ("Best Actor", "Dallas Buyers Club"),
          ("Best Actress", "Blue Jasmine") },),
        { "12 Years a Slave" : 1,
          "Gravity" : 1,
          "Dallas Buyers Club" : 1,
          "Blue Jasmine" : 1 }),
      (({ ("Best Picture", "The King's Speech"),
          ("Best Director", "The King's Speech"),
          ("Best Actor", "The King's Speech") },),
        { "The King's Speech" : 3}),
      (({ ("Best Picture", "Spotlight"), ("Best Director", "The Revenant"),
          ("Best Actor", "The Revenant"), ("Best Actress", "Room"),
          ("Best Supporting Actor", "Bridge of Spies"),
          ("Best Supporting Actress", "The Danish Girl"),
          ("Best Original Screenplay", "Spotlight"),
          ("Best Adapted Screenplay", "The Big Short"),
          ("Best Production Design", "Mad Max: Fury Road"),
          ("Best Cinematography", "The Revenant") },),
        { "Spotlight" : 2,
          "The Revenant" : 3,
          "Room" : 1,
          "Bridge of Spies" : 1,
          "The Danish Girl" : 1,
          "The Big Short" : 1,
          "Mad Max: Fury Road" : 1 }),
       ((set(),), { }),
            ]
    for args,result in tests:
        if (movieAwards(*args) != result):
            print('movieAwards failed:')
            print(args)
            print(result)
            assert(False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)
    print("Passed!")


def testInvertDictionary():
    print("Testing invertDictionary()...", end="")
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
           {2:{1}, 3:{2,5}, 4:{3}})
    print("Passed!")

def testReadDogDataCsvFileInto2dList():
    print('Testing readDogDataCsvFileInto2dList()...', end='')
    data = readDogDataCsvFileInto2dList('2018-abridged')
    assert(data[0] == ['LicenseType','Breed','Color','DogName','OwnerZip',
                       'ExpYear','ValidDate'])
    assert(len(data) == 101)
    assert(data[-1] == ['Dog Senior Citizen or Disability Neutered Male',
                        'YORKSHIRE TERRIER', 'BLACK/BROWN', 'JACK', '15238',
                        '2018', '2017-11-29T09:47:37'])
    print('Passed!')

def testConvert2dListToTable():
    print('Testing convert2dListToTable()...', end='')
    data = readDogDataCsvFileInto2dList('2018-abridged')
    table = convert2dListToTable(data)
    assert(len(data) == len(table))
    assert(data[18] == ['Dog Individual Spayed Female', 'COCKER SPANIEL', 
                        'BLONDE', 'JUILET', '15214', '2018', 
                        '2017-11-27T10:42:11'])
    assert(table[18] == {'LicenseType': 'Dog Individual Spayed Female',
                         'Breed': 'COCKER SPANIEL',
                         'Color': 'BLONDE',
                         'DogName': 'JUILET', 
                         'OwnerZip': '15214', 
                         'ExpYear': '2018', 
                         'ValidDate': '2017-11-27T10:42:11'
                        })
    print("Passed!")

def testCleanData():
    print('Testing cleanData()...', end='')
    data = readDogDataCsvFileInto2dList('2018-abridged')
    table = convert2dListToTable(data)
    cleanData(table) # note this works destructively!
    assert(table[18] == {'LicenseType': 'Female',
                         'Breed': 'Cocker Spaniel',
                         'Color': ['blonde'],
                         'DogName': 'Juilet', 
                         'OwnerZip': '15214', 
                         'ExpYear': 2018, 
                         'ValidDate': 2017
                        })
    # Note that the raw data for row 2 has the Color BLACK/BROWN
    assert(table[2]['Color'] == ['black', 'brown'])
    # Note that the raw data for row 26 has the DogName "CHRISTINA ""TINA"""
    assert(table[26]['DogName'] == 'Christina Tina')
    print('Passed!')

def testGetCleanedTable():
    print('Testing getCleanedTable()...', end='')
    table = getCleanedTable('2018-abridged')
    assert(len(table) == 101)
    assert(table[18] == {'LicenseType': 'Female',
                         'Breed': 'Cocker Spaniel',
                         'Color': ['blonde'],
                         'DogName': 'Juilet', 
                         'OwnerZip': '15214', 
                         'ExpYear': 2018, 
                         'ValidDate': 2017
                        })
    print('Passed!')

def testGetValueSets():
    print('Testing getValueSets()...', end='')
    valueSets = getValueSets('2018-abridged')
    assert(valueSets == {
        'LicenseType': {
            'Unknown', 'Female', 'Male'
            },
        'Breed': {
            'Cockapoo', 'Bichon Frise', 'Boxer Mix', 'Poodle Mix',
            'Am Pitt Bull Mix', 'Brittany Spaniel', 'Beagle', 'Shepherd Mix',
            'Maltese Mix', 'Terrier Mix', 'Morkie', 'Aus Shepherd', 'Tag',
            'Am Pit Bull Terrier', 'Mixed', 'Tree Walk Coonhound',
            'Great Dane', 'Golden Retriever', 'Beagle Mix', 'Shih Tzu',
            'Akita', 'Ger Shepherd', 'Cane Corso', 'Weimaraner',
            'Goldendoodle', 'Poodle Standard', 'Belg Malinois',
            'Ger Shepherd Mix', 'Sib Husky', 'Estrela Mtn Dog', 'Chihuahua',
            'Maltese', 'Doberman Pinscher', 'Rat Terrier',
            'Labrador Retriever', 'Min Pinscher', 'Doberman Mix',
            'Yorkshire Terrier', 'Greyhound', 'Dachshund Mix', 'Keeshond',
            'Shetland Sheepdog', 'Lab Mix', 'Scottish Terrier',
            'Cocker Spaniel', 'Portugese Water Dog', 'Lhasa Apso Mix',
            'Yorkshire Terr Mix', 'Havanese'
            },
        'Color': {
            'grey', '', 'yellow', 'tan', 'brown', 'buff', 'red', 'cream',
            'gold', 'orange', 'brindle', 'blonde', 'spotted', 'multi',
            'black', 'white'},
        'DogName': {
            'Rosie ', 'Tucker', 'Rusty', 'Isis', 'Juilet', 'Gus', 'Romeo',
            'Doggie', 'Taffy', 'Karma', 'Bumble', 'Sable', 'Jessie', 'Lola',
            'Luna', 'Happy', 'Jake', 'Neena', 'Baloo', 'Buddy', 'Maeby Axford',
            'Eich', 'Honey Puck', 'Toby', 'Stella', 'Abe', 'Valkyrie', 'Carly',
            'Chickie', 'Aslan Mcgregor', 'Princess', 'Duke',
            'Rufus Gerald Wallace', 'Emily', 'Nahbi', 'Norman Mitchell',
            'Cissie Bear', 'Hunter', 'Molly Magee', 'Bailey', 'Howie',
            'Zoe Vitsas', 'Bruno', 'Dakota', 'Charley', 'Sisco', 'Molly',
            'Zeta', 'Jack', 'Shadoe', 'Annie', 'Charlie', 'Willie', 'Cobalt',
            'Bear', 'Roxy', 'Saint', 'Lilly', 'Oakley', 'Clover', 'Joe',
            'Christina Tina', 'Chloe', 'Murphy', 'Cooper', 'Tacoda',
            'Mimi Pearl Foster', 'Ellie', 'Tonks', 'Rosie', 'Teddy', 'King',
            'Leroi', 'Dude', 'Arrow', 'Titan', 'Luce', 'Bandit', 'Bojangles',
            'Baley', 'Missy', 'Jackson', 'Sydney', 'Maggie', 'Curious George',
            'Snowball', 'Winnie', 'Madeleine', 'Izzy'
            },
        'OwnerZip': {
            '15120', '15221', '15126', '15131', '15068', '15133', '15218',
            '15129', '15136', '15209', '15147', '15057', '15104', '15108',
            '15227', '15116', '15237', '15018', '15137', '15101', '15236',
            '15017', '15205', '15202', '15148', '15102', '15090', '15234',
            '15220', '15146', '15139', '15228', '15044', '15239', '15042',
            '15135', '15238', '15025', '15214', '15045', '15122', '15106',
            '15241', '15235', '15229'
            },
        'ExpYear': {
            2018
            },
        'ValidDate': {
            2017
            }
        })
    print('Passed!')

def testGetValueCounts():
    print('Testing getValueCounts()...', end='')
    valueCounts = getValueCounts('2018-abridged')
    assert(valueCounts == {
        'LicenseType': {
            'Male': 47, 'Female': 52, 'Unknown': 1
            },
        'Breed': {
            'Cockapoo': 2, 'Ger Shepherd': 4, 'Belg Malinois': 1, 'Mixed': 9, 
            'Am Pit Bull Terrier': 1, 'Scottish Terrier': 1, 
            'Yorkshire Terrier': 4, 'Dachshund Mix': 2, 'Shetland Sheepdog': 2,
            'Labrador Retriever': 5, 'Bichon Frise': 2, 'Lhasa Apso Mix': 1,
            'Am Pitt Bull Mix': 4, 'Brittany Spaniel': 2, 'Terrier Mix': 4,
            'Cocker Spaniel': 3, 'Maltese': 5, 'Lab Mix': 5, 'Havanese': 1,
            'Akita': 1, 'Beagle Mix': 2, 'Doberman Mix': 1, 'Shih Tzu': 2,
            'Ger Shepherd Mix': 1, 'Doberman Pinscher': 1, 'Greyhound': 1,
            'Chihuahua': 1, 'Beagle': 3, 'Morkie': 1, 'Aus Shepherd': 1,
            'Poodle Standard': 1, 'Tree Walk Coonhound': 1, 'Great Dane': 1,
            'Estrela Mtn Dog': 1, 'Boxer Mix': 1, 'Portugese Water Dog': 1,
            'Golden Retriever': 6, 'Maltese Mix': 1, 'Weimaraner': 1,
            'Shepherd Mix': 1, 'Cane Corso': 1, 'Sib Husky': 2,
            'Poodle Mix': 1, 'Rat Terrier': 1, 'Keeshond': 1,
            'Yorkshire Terr Mix': 1, 'Min Pinscher': 1, 'Goldendoodle': 1,
            'Tag': 3
            },
        'Color': {
            'brown': 40, 'black': 42, 'brindle': 3, 'white': 36, 'tan': 7,
            'yellow': 1, 'spotted': 3, 'blonde': 3, 'multi': 3, 'orange': 1, 
            'cream': 2, 'red': 1, 'grey': 3, '': 1, 'gold': 3, 'buff': 1
            },
        'DogName': {
            'Charley': 1, 'Tacoda': 1, 'Eich': 1, 'Arrow': 1, 'Oakley': 1,
            'Bailey': 1, 'Mimi Pearl Foster': 1, 'Leroi': 1, 'Zoe Vitsas': 1,
            'Taffy': 1, 'Dude': 1, 'Chickie': 1, 'King': 1, 'Emily': 1,
            'Ellie': 3, 'Rusty': 1, 'Annie': 1, 'Juilet': 1, 'Romeo': 1,
            'Lola': 3, 'Abe': 1, 'Maggie': 2, 'Buddy': 1, 'Princess': 1,
            'Christina Tina': 1, 'Howie': 1, 'Happy': 1, 'Lilly': 1,
            'Shadoe': 1, 'Sable': 1, 'Nahbi': 1, 'Valkyrie': 1, 'Doggie': 1,
            'Curious George': 1, 'Willie': 1, 'Snowball': 2, 'Honey Puck': 1,
            'Roxy': 1, 'Bumble': 1, 'Bojangles': 1, 'Stella': 1,
            'Norman Mitchell': 1, 'Winnie': 1, 'Molly Magee': 1,
            'Madeleine': 1, 'Bandit': 1, 'Karma': 1, 'Dakota': 1,
            'Clover': 1, 'Titan': 1, 'Luna': 1, 'Maeby Axford': 2,
            'Saint': 1, 'Luce': 1, 'Baloo': 1, 'Rufus Gerald Wallace': 1,
            'Baley': 1, 'Joe': 1, 'Jackson': 1, 'Teddy': 1,
            'Aslan Mcgregor': 1, 'Charlie': 2, 'Murphy': 1, 'Bear': 1,
            'Cooper': 2, 'Rosie ': 1, 'Hunter': 1, 'Zeta': 1, 'Duke': 1,
            'Bruno': 1, 'Molly': 1, 'Tucker': 1, 'Chloe': 1, 'Gus': 1,
            'Rosie': 1, 'Sydney': 1, 'Sisco': 1, 'Izzy': 1, 'Cissie Bear': 1,
            'Neena': 1, 'Toby': 1, 'Jessie': 1, 'Cobalt': 1, 'Isis': 1,
            'Tonks': 1, 'Carly': 1, 'Jake': 1, 'Missy': 3, 'Jack': 1
            },
        'OwnerZip': {
            '15236': 1, '15238': 6, '15104': 1, '15139': 4, '15129': 1,
            '15090': 1, '15101': 2, '15228': 3, '15235': 5, '15108': 5,
            '15120': 2, '15239': 7, '15214': 2, '15218': 4, '15237': 1,
            '15018': 2, '15025': 4, '15017': 1, '15137': 1, '15045': 2, 
            '15131': 1, '15136': 5, '15205': 4, '15122': 1, '15234': 1, 
            '15057': 1, '15241': 3, '15147': 1, '15135': 2, '15044': 3,
            '15126': 1, '15229': 2, '15221': 2, '15102': 1, '15202': 2, 
            '15227': 1, '15148': 1, '15133': 2, '15209': 2, '15146': 1, 
            '15116': 3, '15106': 2, '15042': 1, '15068': 1, '15220': 1
            },
        'ExpYear': {
            2018: 100
            },
        'ValidDate': {
            2017: 100
            }
        })
    print('Passed!')

def testGetMostPopularValues():
    print('Testing getMostPopularValues()...', end='')
    assert(getMostPopularValues('2018-abridged') == {
        'LicenseType': 'Female',
        'Breed': 'Mixed',
        'Color': 'black',
        'DogName': {'Ellie', 'Lola', 'Missy'},
        'OwnerZip': '15239',
        'ExpYear': 2018,
        'ValidDate': 2017
        })
    print('Passed!')

def testSomeMoreDataAnalysis():
    print('Skipping testing for someMoreDataAnalysis().  :-)')

def testDogLicensesDataAnalysis():
    testReadDogDataCsvFileInto2dList()
    testConvert2dListToTable()
    testCleanData()
    testGetCleanedTable()
    testGetValueSets()
    testGetValueCounts()
    testGetMostPopularValues()
    testSomeMoreDataAnalysis()

#################################################
# testAll and main
#################################################

def testAll():
    # All are required (no mild/medium/spicy)
    testMovieAwards()
    testFriendsOfFriends()
    testInvertDictionary()
    testDogLicensesDataAnalysis()

def main():
    cs112_s20_unit8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
