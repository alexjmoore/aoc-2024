leftNums, rightNums = [], []

with open('input.txt') as input:
    while line := input.readline().strip():
        left, right = line.split()
        leftNums.append(int(left.strip()))
        rightNums.append(int(right.strip()))

leftNums.sort()
rightNums.sort()

total = 0
for i in range(len(leftNums)):
    total += abs(leftNums[i] - rightNums[i])

print(f"total: {total}")