# wleoly
# ucmrsa
# utoshon
# rsoslaoc
# kumfce
# sdeefen
# moraac
# rrgalwne
# isnsna
# oimterrm

from collections import Counter

clearedLines = []
clearedWLLines = []

# --- Read in .txt file, clear contents of linebreaks -> "\n" and save into a list variable
def ReadAndClearFromTxt(fileName, outputListName):
    with open(fileName, "r") as f:
        lines = f.readlines()

    linesLength = len(lines)

    for i in range(linesLength):
        outputListName.append(lines[i].replace("\n", ""))
        
def MatchWord(currentWord):
    charDict = Counter(currentWord)
    lastDictKey = list(charDict)[-1]

    for i in range(len(clearedWLLines)):
        compWord = clearedWLLines[i]
        if len(compWord) != len(currentWord):
            continue
        else:
            for x in charDict.keys():
                if x not in compWord:
                    break
                else: 
                    print(x)
                    for y in charDict.values():
                        if compWord.count(x) != y:
                            break
                        else:
                            if compWord.count(x) == y and x == lastDictKey:
                                return (compWord)

ReadAndClearFromTxt("input_example.txt", clearedLines)
ReadAndClearFromTxt("wordlist.txt", clearedWLLines)

answerWordList = []

for i in range(len(clearedLines)):
    currentWord = clearedLines[i]
    matchWord = MatchWord(currentWord)
    answerWordList.append(matchWord)
    
print(answerWordList)