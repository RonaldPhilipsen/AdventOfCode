import re
from advent_of_code import get_input

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def part1(input_str: str) -> int:
    REPEAT = re.compile(r"^(\d+?)\1$")
    ranges = input_str.split(",")
    total = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if REPEAT.match(str(n)):
                total += n
    return total


def part2(input_str: str) -> int:
    REPEAT = re.compile(r"^(\d+?)\1+$")
    ranges = input_str.split(",")
    total = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if REPEAT.match(str(n)):
                total += n
    return total


part1_result = part1(example)
print(f"Part 1 Example: {part1_result}")
lines = get_input(2025, 2)
part1_result = part1(lines)
print(f"Part 1: {part1_result}")
part2_result = part2(example)
print(f"Part 2 Example: {part2_result}")
part2_result = part2(lines)
print(f"Part 2: {part2_result}")
