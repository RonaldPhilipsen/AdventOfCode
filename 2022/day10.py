from advent_of_code import get_input
from typing import List


INTERESTING_PCS = [20, 60, 100, 140, 180, 220]


class Communicator:
    def __init__(self) -> None:
        self.x = 1
        self.pc = 0
        self.interesting_values = []
        pass

    def __check_if_value_is_interesting(self):
        if self.pc in INTERESTING_PCS:
            self.interesting_values.append(self.pc * self.x)

    def __do_noop(self):
        self.pc += 1
        self.__check_if_value_is_interesting()

    def __addx(self, value: int):
        self.__do_noop()
        self.pc += 1
        self.x += value
        self.__check_if_value_is_interesting()

    def execute_commands(self, input_list: List[str]):
        for i in range(0, len(input_list)):
            command = input_list[i]
            if command == "noop":
                self.__do_noop()
                continue

            opcode, value = command.split()
            if opcode == "addx":
                self.__addx(int(value))

    def get_interesting_values(self):
        return self.interesting_values


input_text = get_input(10).strip()
input_list = input_text.split('\n')

comms = Communicator()
comms.execute_commands(input_list)
interesting_values = comms.get_interesting_values()
sum(interesting_values)
