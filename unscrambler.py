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

rawLines = []
clearedLines = []

with open("input_example.txt", "r") as f:
    lines = f.readlines()

initialLinesCount = len(lines)

for i in range(initialLinesCount):
    clearedLines.append(lines[i].replace("\n", ""))

# test result
print(clearedLines)
