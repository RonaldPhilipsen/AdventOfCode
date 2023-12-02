from advent_of_code import get_input

from functools import cmp_to_key


pairs = [[eval(l) for l in x.split()] for x in get_input(13).split("\n\n")]


def is_correct_order(l: list | int, r: list | int):
    if isinstance(l, int) and isinstance(r, int):
        return l - r

    if isinstance(l, list) and isinstance(r, list):
        if len(l) == 0 and len(r) == 0:
            return 0
        if len(l) == 0:
            return -1
        if len(r) == 0:
            return 1
        r1 = is_correct_order(l[0], r[0])
        return r1 if r1 != 0 else is_correct_order(l[1:], r[1:])
    return is_correct_order([l], r) if isinstance(l, int) else is_correct_order(l, [r])


print(sum(i for i, (l, r) in enumerate(pairs, start=1) if is_correct_order(l, r) < 0))

flat_list = [item for sublist in pairs for item in sublist]
flat_list.extend([[[2]], [[6]]])

pairs_sorted = sorted(flat_list, key=cmp_to_key(is_correct_order))
i1, i2 = pairs_sorted.index([[2]]) + 1, pairs_sorted.index([[6]]) + 1
print(i1 * i2)
