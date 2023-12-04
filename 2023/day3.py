from collections import defaultdict
from functools import reduce
from operator import mul
from advent_of_code import get_input
import re

example_input = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

symbols = {"*", "#", "+", "$"}


input = get_input(2023, 3)

lines = input.strip().splitlines()


nre = re.compile("(\d+)")

S = 0
G = defaultdict(list)

for x, u in enumerate(lines):
    for m in nre.finditer(u):
        num = int(m.group(1))
        add = False

        B = max(x - 1, 0)
        E = min(x + 1, len(lines) - 1)
        b = max(0, m.start(1) - 1)
        e = min(m.end(1), len(u) - 1)

        for row in range(B, E + 1):
            for pos in range(b, e + 1):
                c = lines[row][pos]
                if c != "." and not c.isdigit():
                    add = True
                    if c == "*":
                        G[(row, pos)].append(num)

        if add:
            S += num

print(S)
print(sum([reduce(mul, x) for x in G.values() if len(x) == 2]))
