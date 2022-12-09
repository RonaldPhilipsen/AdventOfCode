from advent_of_code import get_input

DIRECTIONS = {'U': -1J, 'D': 1J, 'L': -1, 'R': 1}


def sign(num: complex):
    return complex((num.real > 0) - (num.real < 0), (num.imag > 0) - (num.imag < 0))


def get_new_tail_pos(head: complex, tail: complex):
    diff = head - tail
    if abs(diff) >= 2:
        tail += complex(sign(diff.real), sign(diff.imag))
    return tail


def move_snake(data, tail_size):
    snake = [0] * (1 + tail_size)
    tail_seen = set()
    for line in data:
        cmd, size = line.split()
        for _ in range(int(size)):
            snake[0] += DIRECTIONS[cmd]
            for i, tail in enumerate(snake[1:], 1):
                snake[i] = get_new_tail_pos(snake[i-1], tail)
            tail_seen.add(snake[-1])
    return len(tail_seen)


if __name__ == '__main__':
    input_str = get_input(9).strip()
    input_list = input_str.split('\n')

    print(move_snake(input_list, 1))
