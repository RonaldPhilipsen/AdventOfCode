from typing import Dict
from advent_of_code import get_input
from functools import cache
from frozenlist import FrozenList

input = get_input(2023, 4)
example_input = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


lines: FrozenList[str] = FrozenList(example_input.strip().splitlines())
lines.freeze()


@cache
def get_n_matching_numbers(line: str):
    winning_numbers_str, my_numbers_str = line.split(":")[1].split("|")
    winning_numbers = winning_numbers_str.split()
    my_numbers = my_numbers_str.split()
    return sum(x in winning_numbers for x in my_numbers)


def part1():
    total_value = 0
    for line in lines:
        n_winning_numbers = get_n_matching_numbers(line)
        if n_winning_numbers == 0:
            continue
        card_value = pow(2, n_winning_numbers - 1)
        total_value += card_value
    print(total_value)


debug_card_dict: Dict[str, int] = {}


@cache
def get_n_scratchcards(lines: FrozenList[str], line_num: int):
    print(line_num)
    debug_card_dict[f"card {line_num+1}"] = (
        (debug_card_dict[f"card {line_num+1}"] + 1)
        if f"card {line_num+1}" in debug_card_dict.keys()
        else 1
    )
    new_scratchards = get_n_matching_numbers(line=lines[line_num])
    total_new_scratchcards = new_scratchards  # also count current scratcard
    for i in range(1, new_scratchards + 1):
        scratch_cards = get_n_scratchcards(lines=lines, line_num=line_num + i)
        total_new_scratchcards += scratch_cards

    return total_new_scratchcards


def part2():
    n_scratch_cards = len(lines)
    for i, _val in enumerate(lines):
        n_scratch_cards += get_n_scratchcards(lines=lines, line_num=i)
    print(n_scratch_cards)


# part1()
part2()
