from advent_of_code import get_input

from functools import cmp_to_key


pairs = [[eval(line) for line in x.split()] for x in get_input(2022, 13).split("\n\n")]


def is_correct_order(left: list | int, right: list | int):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return 0
        if len(left) == 0:
            return -1
        if len(right) == 0:
            return 1
        r1 = is_correct_order(left[0], right[0])
        return r1 if r1 != 0 else is_correct_order(left[1:], right[1:])
    return is_correct_order([left], right) if isinstance(left, int) else is_correct_order(left, [right])


print(sum(i for i, (left, right) in enumerate(pairs, start=1) if is_correct_order(left, right) < 0))

flat_list = [item for sublist in pairs for item in sublist]
flat_list.extend([[[2]], [[6]]])

pairs_sorted = sorted(flat_list, key=cmp_to_key(is_correct_order))
i1, i2 = pairs_sorted.index([[2]]) + 1, pairs_sorted.index([[6]]) + 1
print(i1 * i2)
