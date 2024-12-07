def is_safe_sequence(levels):
    if len(levels) <= 1:
        return True

    direction = None
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if not (1 <= abs(diff) <= 3):
            return False
        if direction is None:
            direction = diff > 0
        elif (diff > 0) != direction:
            return False

    return True

def check_line(levels):
    if is_safe_sequence(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(new_levels):
            return True

    return False

def main():
    safe_count = 0
    with open('input.txt') as input:
        while line := input.readline().strip():
            levels = [int(x) for x in line.strip().split()]
            if check_line(levels):
                safe_count += 1
    print(f"safe: {safe_count}")

if __name__ == "__main__":
    main()