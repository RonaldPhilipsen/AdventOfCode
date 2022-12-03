from advent_of_code import get_input
from typing import List


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_priority(item: str) -> int:
    """Gets the priority for the elves

    Args:
        item (str): the character to get the priority for

    Returns:
        int: the priority for the item
    """
    if str.isupper(item):
        prio = ord(item) - ord('A') + 27
    else:
        prio = ord(item) - ord('a') + 1
    return prio


def do_part_1(input_list: List[str]):
    priorities = []
    for backpack in input_list:
        first_compartment = slice(0, len(backpack)//2)
        second_compartment = slice(len(backpack)//2, len(backpack))
        s1 = set(backpack[first_compartment])
        s2 = set(backpack[second_compartment])
        overlap = list(s1.intersection(s2))

        for item in overlap:
            priorities.append(get_priority(item))

    print(f'Total priories for all elves {sum(priorities)}')


def do_part_2(input_list: List[str]):
    group_priorities = []
    groups = list(chunks(input_list, 3))
    for group in groups:
        sticker = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        if len(sticker) > 1:
            raise Exception("More than one matching item in group")
        if len(sticker) == 0:
            raise Exception("elves have no group :(")
        group_priorities.append(get_priority(sticker.pop()))
    print(f'total group priorities: {sum(group_priorities)}')


if __name__ == "__main __":
    input_str = get_input(3)
    input_list = input_str.split('\n')
    do_part_1(input_list)
    do_part_2(input_list)
