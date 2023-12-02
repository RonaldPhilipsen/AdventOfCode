import regex
from typing import Dict
from advent_of_code import get_input


input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

numbers: Dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


input = get_input(2023, 1)


def part1():
    total_calibration_values = 0

    for line in input.splitlines():
        if not line:
            continue
        digits = regex.findall(r"(\d)", line, overlapped=True)
        assert digits

        firstdigit = digits[0]

        if len(digits) == 1:
            lastdigit = firstdigit
        else:
            lastdigit = digits[-1]

        calibrationval = int(firstdigit + lastdigit)
        total_calibration_values += calibrationval
    print(total_calibration_values)


def part2():
    total_calibration_values = 0

    for line in input.splitlines():
        if not line:
            continue
        digits = regex.findall(
            rf'(\d|{"|".join(numbers.keys())})', line, overlapped=True
        )
        assert digits

        firstdigit = numbers[digits[0]] if digits[0] in numbers else digits[0]

        if len(digits) == 1:
            lastdigit = firstdigit
        else:
            lastdigit = numbers[digits[-1]] if digits[-1] in numbers else digits[-1]

        calibrationval = int(firstdigit + lastdigit)
        total_calibration_values += calibrationval

    print(total_calibration_values)
