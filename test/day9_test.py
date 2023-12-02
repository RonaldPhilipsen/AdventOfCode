import unittest
from day9 import get_new_tail_pos, move_snake


class TestUpdate_tail_pos(unittest.TestCase):
    def test_2_right(self):
        head = 2
        tail = 0
        new_tail_pos = get_new_tail_pos(head, tail)
        assert new_tail_pos == 1

    def test_2_left(self):
        head = -2
        tail = 0
        new_tail_pos = get_new_tail_pos(head, tail)
        assert new_tail_pos == -1

    def test_2_up(self):
        head = 0 + 2j
        tail = 0
        new_tail_pos = get_new_tail_pos(head, tail)
        assert new_tail_pos == 1j

    def test_2_down(self):
        head = 0 - 2j
        tail = 0
        new_tail_pos = get_new_tail_pos(head, tail)
        assert new_tail_pos == -1j

    def test_diagonal_up(self):
        head = 4 + 3j
        tail = 2 + 2j
        new_tail_pos = get_new_tail_pos(head, tail)
        assert new_tail_pos == 3 + 3j

    def test_diagonal_right(self):
        head = 4 + 3j
        tail = 2 + 2j
        new_tail_pos = get_new_tail_pos(head, tail)
        assert new_tail_pos == 3 + 3j

    def test_part1(self):
        INPUT_S = [
            "R 4",
            "U 4",
            "L 3",
            "D 1",
            "R 4",
            "D 1",
            "L 5",
            "R 2",
        ]
        output = move_snake(INPUT_S, 1)
        assert output == 13


if __name__ == "__main__":
    unittest.main()
