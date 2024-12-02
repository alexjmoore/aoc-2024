safeCount = 0

def checkLine(levels):
    increasing = False
    errorCount = 0
    if levels[0] < levels[1]: increasing = True
    for i in range(1, len(levels)):
        curr = levels[i-1]
        next = levels[i]
        if increasing:
            if (next <= curr):
                errorCount+=1
        else:
            if (next >= curr):
                errorCount+=1
        if  1 < abs(curr - next) > 3:
            errorCount+=1
    return errorCount

with open('input.txt') as input:
    while line := input.readline().strip():
        levels =  [int(x) for x in line.split()]
        if checkLine(levels) <= 1:
            safeCount+=1
            
print(f"safe: {safeCount}")