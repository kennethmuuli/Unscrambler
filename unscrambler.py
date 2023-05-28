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

clearedLines = []

# --- Read in .txt file, clear contents of linebreaks -> "\n" and save into a list variable
def ReadAndClearFromTxt(fileName, outputListName):
    with open(fileName, "r") as f:
        lines = f.readlines()

    initialLinesCount = len(lines)

    for i in range(initialLinesCount):
        outputListName.append(lines[i].replace("\n", ""))

ReadAndClearFromTxt("input_example.txt", clearedLines)

# test result
print(clearedLines)

