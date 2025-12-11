from advent_of_code import get_input

example = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


def part1(lines: list[str]):
    total_joltage = 0
    for line in lines:
        d1 = max(line)
        index = line.index(d1)
        if index == len(line) - 1:
            d1, d2 = max(line[:-1]), d1
        else:
            d2 = max(line[index + 1 :])
        line_joltage = d1 + d2
        total_joltage += int(line_joltage)
    return total_joltage


N_CHARACTERS = 12


def part2(lines: list[str]):
    total_joltage = 0
    for line in lines:
        chars = []
        for i in range(N_CHARACTERS):
            left = 0
            for j in range(1, len(line) - (N_CHARACTERS - i) + 1):
                if line[j] > line[left]:
                    left = j
            chars.append(line[left])
            line = line[left + 1 :]
        total_joltage += int("".join(chars))
    return total_joltage


part1_result = part1(example)
print(f"Part 1 Example: {part1_result}")
lines = get_input(2025, 3)
part1_result = part1(lines.splitlines())
print(f"Part 1: {part1_result}")
part2_result = part2(example)
print(f"Part 2 Example: {part2_result}")
part2_result = part2(lines.splitlines())
print(f"Part 2: {part2_result}")
