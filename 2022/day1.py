from advent_of_code import get_input


if __name__ == "__main __":
    """do the counting calories exercise"""
    input_str = get_input(1).strip()
    input_list = input_str.split("\n")
    elf = []
    elves = []  # type: List[int]
    for line in input_list:
        if line:
            elf.append(int(line))
        else:
            elves.append(elf)
            elf = []
    elves.append(elf)

    total_calories = [sum(elf) for elf in elves]
    total_calories.sort(reverse=True)

    print(f"max_calories: {total_calories[0]}")
    print(f"top 3 calories: {sum(total_calories[0:3])}")
