#! /bin/python3

import math
import re
from typing import Sequence
from advent_of_code import get_input

DIGITS = r"\d+"

example_input = """\
Time:      7  15   30
Distance:  9  40  200
"""



def part1(lines: Sequence[str]):
    times = map(int, re.findall(DIGITS, lines[0]))
    records = map(int, re.findall(DIGITS, lines[1]))
    options = list()
    for time, record in zip(times, records):
        j,count = 0, 0
        for i in range(time):
            distance = i * (time - j)

            if distance > record:
                count += 1
            j += 1
        options.append(count)
    print(math.prod(options))
    
def part2(lines: Sequence[str]):
    time = int(lines[0].split(':')[1].replace(' ', '', -1))
    record = int(lines[1].split(':')[1].replace(' ', '', -1))
    
    j = 0
    count = 0
    for i in range(time):
        distance = i * (time - j)

        if distance > record:
            count += 1
        j += 1

    print(count)

input = get_input(2023, 6)
lines: Sequence[str] = input.splitlines()
part1(lines)
part2(lines)