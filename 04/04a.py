
grid = []

def findXmasMask(x, y, maskx, masky):
    if (0 <= (x+(maskx*3)) < len(grid[0])) and (0 <= (y+(masky*3)) < len(grid)):
        if grid[y+masky][x+maskx] == "M" and grid[y+(masky*2)][x+(maskx*2)] == "A" and grid[y+(masky*3)][x+(maskx*3)] == "S":
            return True
    return False

def findXmas(x,y):
    found = 0
    if findXmasMask(x, y, 0, 1): found += 1
    if findXmasMask(x, y, 0, -1): found += 1
    if findXmasMask(x, y, 1, 0): found += 1
    if findXmasMask(x, y, -1, 0): found += 1
    if findXmasMask(x, y, 1, 1): found += 1
    if findXmasMask(x, y, 1, -1): found += 1
    if findXmasMask(x, y, -1, 1): found += 1
    if findXmasMask(x, y, -1, -1): found += 1
    return found

def main():
    total = 0
    with open('input.txt') as input:
        while line := input.readline().strip():
            grid.append(line)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "X":
                    total += findXmas(x,y)
        print(f"total: {total}")

if __name__ == "__main__":
    main()