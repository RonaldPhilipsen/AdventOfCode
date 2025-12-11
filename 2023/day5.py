#! /bin/python3


from advent_of_code import get_input
import re


example_input = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2        res = input.strip().split("\n\n")
        seeds = list(map(int, re.findall(r"\d+", res[0])))
        ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
        for cs in res[1:]:
            c = list(map(int, re.findall(r"\d+", cs)))
            # sort for part 2
            cv = sorted([c[k : k + 3] for k in range(0, len(c), 3)], key=lambda x: x[1])
            seeds = [getNextAmount(cv, s) for s in seeds]
            ranges = sum((getNextRanges(cv, rng) for rng in ranges), [])
        print(min(seeds), next(map(min, zip(*ranges))))


39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def getNextAmount(cv, seed):
    for c in cv:
        if c[1] <= seed < c[1] + c[2]:
            return c[0] - c[1] + seed
    return seed


def getNextRanges(cv, rng):
    ranges, i = [], 0
    while True:
        c = cv[i]
        if c[1] > rng[0]:
            if c[1] > rng[1]:
                ranges.append(rng)
                return ranges
            ranges.append((rng[0], c[1] - 1))
            rng = c[1], rng[1]
        elif c[1] <= rng[0] < c[1] + c[2]:
            offset = c[0] - c[1]
            if rng[1] < c[1] + c[2]:
                ranges.append(tuple(r + offset for r in rng))
                return ranges
            ranges.append((rng[0] + offset, c[0] + c[2]))
            rng = c[1] + c[2], rng[1]
        elif c[1] + c[2] <= rng[0]:
            i += 1
            if i == len(cv):
                break
    ranges.append(rng)
    return ranges


def main():
    input = get_input(2023, 5)
    res = input.strip().split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", res[0])))
    ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for cs in res[1:]:
        c = list(map(int, re.findall(r"\d+", cs)))
        # sort for part 2
        cv = sorted([c[k : k + 3] for k in range(0, len(c), 3)], key=lambda x: x[1])
        seeds = [getNextAmount(cv, s) for s in seeds]
        ranges = sum((getNextRanges(cv, rng) for rng in ranges), [])
    print(min(seeds), next(map(min, zip(*ranges))))


if __name__ == """__main__""":
    main()
