from typing import Dict
from advent_of_code import get_input

lines = get_input(2024, 1).splitlines()
# lines = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """.splitlines()

left = []
right = []


def part1() -> int:
    for line in lines:
        print(line)
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()
    res = 0
    for i in range(len(left)):
        res += abs(right[i] - left[i])
    return res


def part2() -> int:
    n_occurrences: Dict[int, int] = {}
    for value in right:
        if value in n_occurrences:
            n_occurrences[value] += 1
        else:
            n_occurrences[value] = 1

    res = 0
    for val in left:
        if val in n_occurrences:
            intermediate = val * n_occurrences[val]
            print(intermediate)
            res += intermediate
    return res


print(part1())
print(part2())
