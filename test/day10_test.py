from day10 import Communicator
import unittest


class TestFindInterestingValues(unittest.TestCase):
    def test_sample_input(self):
        input_list = []
        with open('test\day10_sample_input.txt') as f:
            input_text = f.read().strip()
            input_list = input_text.split('\n')

        comms = Communicator()
        comms.execute_commands(input_list)
        interesting_values = comms.get_interesting_values()

        print(interesting_values)
        assert sum(interesting_values) == 13140
        assert interesting_values == [420, 1140, 1800, 2940, 2880, 3960]
