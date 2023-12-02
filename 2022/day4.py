from advent_of_code import get_input

input_str = get_input(4).strip()
input_list = input_str.split('\n')


def fully_contains(a_set: set, b_set: set):
    return a_set.issubset(b_set) or a_set.issuperset(b_set)


def overlaps(a_set: set, b_set: set):
    ans = a_set.intersection(b_set)
    return len(ans) >= 1


n_fully_contains = 0
n_overlaps = 0
for ip in input_list:
    a, b = ip.split(',')
    a_min, a_max = a.split('-')
    b_min, b_max = b.split('-')
    a_set = set(range(int(a_min), int(a_max) + 1))
    b_set = set(range(int(b_min), int(b_max) + 1))

    if fully_contains(a_set, b_set):
        n_fully_contains += 1
    if overlaps(a_set, b_set):
        n_overlaps += 1

print(n_fully_contains)
print(n_overlaps)
