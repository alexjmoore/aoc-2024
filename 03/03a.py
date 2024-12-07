import re
def main():
    total = 0
    with open('input.txt') as input:
        line = input.read()
        valid_instructions = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', line)
        total += sum([int(x) * int(y) for x, y in valid_instructions])
    print(f"total: {total}")

if __name__ == "__main__":
    main()