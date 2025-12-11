from advent_of_code import get_input

lines = get_input(2025, 1).splitlines()

DIAL_START = 50
LOOKUP_NUMBER = 0

example = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


def part1(instructions):
    number_of_zeroes = 0
    position = DIAL_START
    for instruction in instructions:
        turn = instruction[0]
        amount = int(instruction[1:])
        if turn == "L":
            position -= amount
        elif turn == "R":
            position += amount
        position %= 100
        if position == LOOKUP_NUMBER:
            number_of_zeroes += 1
    return number_of_zeroes


def part2(instructions):
    count = 0
    pos = DIAL_START
    for instruction in instructions:
        turn = instruction[0]
        amount = int(instruction[1:])

        count += amount // 100
        amount = amount % 100

        if amount:
            prev = pos
            if turn == "L":
                pos -= amount
                if pos <= 0 < prev:
                    count += 1
            else:
                pos += amount
                if pos >= 100:
                    count += 1
            pos %= 100

    return count


part1_result = part1(example)
print(f"Part 1 Example: {part1_result}")
part1_result = part1(lines)
print(f"Part 1: {part1_result}")
part2_result = part2(example)
print(f"Part 2 Example: {part2_result}")
part2_result = part2(lines)
print(f"Part 2: {part2_result}")
