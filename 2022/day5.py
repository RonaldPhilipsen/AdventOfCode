from advent_of_code import get_input
from typing import List
import re


def parse_header(input_list: List[str]):
    w = 9
    stacks = [[] for x in range(w)]
    row = 0
    while input_list[row]:
        if input_list[row] == ' 1   2   3   4   5   6   7   8   9 ':
            break
        for column in range(1, 10):
            box = input_list[row][((4*column) - 4): (4*column)]
            if not box.isspace():
                stacks[column - 1].insert(0,box)
        row += 1
    return stacks, row+2


def print_first_letter_of_each_column(mat: List[List[str]]):
    for column in mat:
        tmp = column.pop()
        print(tmp[1:2], end='')
        column.append(tmp)
    print()


def do_part1(input_list):
    mat, start = parse_header(input_list)
    for i in range(start, len(input_list)):
        "move 1 from 2 to 1"
        match = re.match(r'move (\d+) from (\d+) to (\d+)', input_list[i])
        if not match:
            continue
        num_crates = int(match.group(1))
        from_column = int(match.group(2))
        to_column = int(match.group(3))
        for i in range(num_crates):
            tmp = mat[from_column - 1].pop()
            mat[to_column - 1].append(tmp)
    print_first_letter_of_each_column(mat)


def do_part2(input_list):
    mat, start = parse_header(input_list)
    for i in range(start, len(input_list)):
        "move 1 from 2 to 1"
        match = re.match(r'move (\d+) from (\d+) to (\d+)', input_list[i])
        if not match:
            continue
        num_crates = int(match.group(1))
        from_column = int(match.group(2))
        to_column = int(match.group(3))
        claw = []
        for i in range(num_crates):
            tmp = mat[from_column - 1].pop()
            claw.append(tmp)
        for i in range(len(claw)):
            tmp = claw.pop()
            mat[to_column - 1].append(tmp)

    print_first_letter_of_each_column(mat)


if __name__ == '__main__':
    input_str = get_input(5)
    input_list = input_str.split('\n')
    do_part1(input_list)
    do_part2(input_list)
