import collections

grid = []
aTracker = collections.defaultdict(int)

def findXmasMask(x, y, maskx, masky):
    if (0 <= (x+(maskx*2)) < len(grid[0])) and (0 <= (y+(masky*2)) < len(grid)):
        if grid[y+masky][x+maskx] == "A" and grid[y+(masky*2)][x+(maskx*2)] == "S":
            aTracker[(y+masky, x+maskx)] += 1
            return True
    return False

def findXmas(x,y):
    findXmasMask(x, y, 1, 1)
    findXmasMask(x, y, 1, -1)
    findXmasMask(x, y, -1, 1)
    findXmasMask(x, y, -1, -1)

def main():
    total = 0
    with open('input.txt') as input:
        while line := input.readline().strip():
            grid.append(line)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "M":
                    findXmas(x,y)
        
        for i in aTracker:
            if aTracker[i] > 1:
                total+= 1
        print(f"total: {total}")

if __name__ == "__main__":
    main()