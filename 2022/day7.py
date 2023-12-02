import re
from advent_of_code import get_input


class Directory:
    def __init__(self, parent: "Directory") -> None:
        self.parent = parent
        self.directories = {}  # type:  dict[str, Directory]
        self.files = {}  # type:  dict[str, int]

    def get_size(self):
        file_size = sum(self.files.values())
        dict_size = sum(
            [directory.get_size() for directory in self.directories.values()]
        )
        return file_size + dict_size


def get_directories(input_list):
    root = Directory(None)
    current_dir = root

    directories = []

    for line in input_list:
        if line.startswith("$ cd"):
            m = re.match(r"\$ cd (.*)", line)
            if not m:
                raise Exception("Failed to parse cd command")

            selected_dir = m.group(1)

            if selected_dir == "/":
                current_dir = root
            elif selected_dir == "..":
                current_dir = current_dir.parent
            else:
                if selected_dir not in current_dir.directories:
                    raise Exception("Tried to cd to directory that doesn´t exist")
                current_dir = current_dir.directories[selected_dir]
            continue
        if line == "$ ls":
            continue

        m = re.match(r"dir (.*)", line)
        if m:
            current_dir.directories[m.group(1)] = Directory(current_dir)
            directories.append(current_dir.directories[m.group(1)])
            continue

        size, name = line.split(" ")
        current_dir.files[name] = int(size)
    return root, directories


if __name__ == "__main__":
    input_str = get_input(7).strip()
    input_list = input_str.split("\n")
    root, directories = get_directories(input_list)

    part1 = sum(
        [
            directory.get_size()
            for directory in directories
            if directory.get_size() < 100000
        ]
    )
    print(part1)

    TOTAL_DISK_SPACE = 70000000
    NEEDED_DISK_SPACE = 30000000

    current_disk_usage = root.get_size()
    current_free_space = TOTAL_DISK_SPACE - current_disk_usage
    need_to_remove = NEEDED_DISK_SPACE - current_free_space

    part2 = min(
        [
            directory.get_size()
            for directory in directories
            if directory.get_size() > need_to_remove
        ]
    )
    print(part2)
