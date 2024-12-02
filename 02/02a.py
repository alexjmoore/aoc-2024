safeCount = 0

with open('input.txt') as input:
    while line := input.readline().strip():
        levels =  [int(x) for x in line.split()]
        increasing = False
        isSafe = True
        if levels[0] < levels[1]: increasing = True
        for i in range(1, len(levels)):
            curr = levels[i-1]
            next = levels[i]
            if increasing:
                if (next <= curr):
                    isSafe = False
                    break
            else:
                if (next >= curr):
                    isSafe = False
                    break
            if  1 < abs(curr - next) > 3:
                isSafe=False
                break
        if isSafe:
            safeCount+=1
            
print(f"safe: {safeCount}")