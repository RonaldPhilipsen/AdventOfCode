from advent_of_code import get_input


def find_start_bit(input_str, sequence_len):
    for i in range(0, len(input_str)):
        st = set(input_str[i : i + sequence_len])
        if (len(st)) == sequence_len:
            return i + sequence_len


if __name__ == "__main__":
    input_str = get_input(6).strip()
    find_start_bit(input_str, 4)
    find_start_bit(input_str, 14)
