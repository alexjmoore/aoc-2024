leftNums, rightNums = [], []

with open('example.txt') as input:
    while line := input.readline().strip():
        left, right = line.split()
        leftNums.append(int(left.strip()))
        rightNums.append(int(right.strip()))

total = 0
for i in range(len(leftNums)):
    total += leftNums[i] * rightNums.count(leftNums[i])

print(f"total: {total}")