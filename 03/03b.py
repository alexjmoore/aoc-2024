import re

def sumInstructions(instructions):
    return sum([int(x) * int(y) for x, y in instructions])

def getTuples(instructions):
    return re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', instructions)

def main():
    total = 0
    with open('input.txt') as input:
        line = input.read()
        split = re.split(r'don\'t\(\)', line)
        print(len(split))
        # always starts enabled
        total += sumInstructions(getTuples(split.pop(0)))
        for block in split:
            instructions = re.split(r'do\(\)', block)
            # ignore the don't block
            instructions.pop(0)
            for i in instructions:
                total += sumInstructions(getTuples(i))
    print(f"total: {total}")

if __name__ == "__main__":
    main()