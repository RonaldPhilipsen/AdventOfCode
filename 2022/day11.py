from advent_of_code import get_input
from typing import List
import re
import math
from copy import deepcopy
from dataclasses import dataclass
from functools import reduce
from operator import mul

class Monkey:
    def __init__(
        self,
        starting_items: List[int],
        operation,
        divisible_by: int,
        if_true: int,
        if_false: int,
    ) -> None:
        self.items = starting_items
        self.operation = operation
        self.divisible_by = divisible_by
        self.throw_to_true = if_true
        self.throw_to_false = if_false
        self.n_inspections = 0
        pass

    def __do_operation(self, value):
        if operation[0] == "old":
            a = value
        else:
            a = int(operation[0])
        if operation[2] == "old":
            b = value
        else:
            b = int(operation[2])

        if operation[1] == "+":
            return a + b
        elif operation[1] == "-":
            return a - b
        elif operation[1] == "*":
            return a * b

    def inspect(self):
        throw_true = []
        throw_false = []
        for item in self.items:
            worry = self.__do_operation(item)
            worry = math.floor(worry / 3)
            if worry % self.divisible_by == 0:
                throw_true.append(worry)
            else:
                throw_false.append(worry)
            self.n_inspections += 1
        self.items.clear()
        return throw_true, throw_false


input_text = get_input(11).strip()
input_list = input_text.split("\n")
monkeys = []  # type: List[Monkey]

split_by_monkeys = input_text.split("Monkey")

for monkey in split_by_monkeys:
    if not monkey:
        continue

    lines = monkey.split("\n")

    monkey_no = int(lines[0][1])
    starting_items = [int(number) for number in lines[1].split(":")[1].split(",")]
    operation = re.match(r"\s*Operation: new = (.*)\s([+*])\s(.*)", lines[2]).groups()
    divisible_by = int(re.match(r"\s*Test: divisible by (\d*)", lines[3]).group(1))
    if_true = int(re.match(r"\s*If true: throw to monkey\s(\d)", lines[4]).group(1))
    if_false = int(re.match(r"\s*If false: throw to monkey\s(\d)", lines[5]).group(1))

    monkeys.append(Monkey(starting_items, operation, divisible_by, if_true, if_false))


for i in range(0, 20):
    for monkey in monkeys:
        throw_true, throw_false = monkey.inspect()
        monkeys[monkey.throw_to_true].items.extend(throw_true)
        monkeys[monkey.throw_to_false].items.extend(throw_false)

n_inspections = [monkey.n_inspections for monkey in monkeys]
n_inspections.sort(reverse=True)
print(n_inspections[0] * n_inspections[1])



data = input_text


@dataclass(frozen=True)
class MonkeyRule:
    expr: str
    test: int
    destination_if_true: int
    destination_if_false: int


@dataclass
class MonkeyState:
    items: list
    inspection_count: int = 0


rules = []
initial_state = []


def parse_monkey(spec):
    global rules, initial_state

    lines = spec.split("\n")

    items = [int(x) for x in lines[1].split(": ")[1].split(", ")]
    initial_state.append(MonkeyState(items))

    expr = lines[2].split(": new = ")[1]
    test = int(lines[3].split("by ")[1])
    destination_if_true = int(lines[4].split("monkey ")[1])
    destination_if_false = int(lines[5].split("monkey ")[1])

    rule = MonkeyRule(expr, test, destination_if_true, destination_if_false)
    rules.append(rule)


specs = data.split("\n\n")
for spec in specs:
    parse_monkey(spec)

states = deepcopy(initial_state)


def do_turn(i, should_divide, magic):
    global rules, state

    rule = rules[i]
    state = states[i]

    while state.items:
        state.inspection_count += 1
        _old = state.items.pop(0)
        new = eval(rule.expr)
        if should_divide:
            new //= 3
        else:
            new %= magic
        if new % rule.test == 0:
            states[rule.destination_if_true].items.append(new)
        else:
            states[rule.destination_if_false].items.append(new)


def viz_states():
    for i in range(len(rules)):
        print(f"Monkey {i}: ", end="")
        print(", ".join(str(x) for x in states[i].items))


def do_round(should_divide=True, magic=-1):
    global rules, state

    for i in range(len(rules)):
        do_turn(i, should_divide, magic)


for _ in range(20):
    do_round()

counts = sorted((state.inspection_count for state in states), reverse=True)
print(counts[0] * counts[1])

states = deepcopy(initial_state)

magic = reduce(mul, (rule.test for rule in rules))

for _ in range(10000):
    do_round(should_divide=False, magic=magic)

counts = sorted((state.inspection_count for state in states), reverse=True)
print(counts[0] * counts[1])
