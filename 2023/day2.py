from advent_of_code import get_input
import re
from collections import namedtuple

exampleInput = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

N_RED, N_GREEN, N_BLUE = 12, 13, 14


def parse_input(input: str):
    lines = input.splitlines()
    result = []
    Game = namedtuple("Game", ["num", "red", "green", "blue"])
    for line in lines:
        num = int(re.findall(r"Game \d+", line.strip())[0].split()[-1])
        reds = list(
            map(lambda x: int(x.split()[0]), re.findall(r"\d+ red", line.strip()))
        )
        greens = list(
            map(lambda x: int(x.split()[0]), re.findall(r"\d+ green", line.strip()))
        )
        blues = list(
            map(lambda x: int(x.split()[0]), re.findall(r"\d+ blue", line.strip()))
        )
        result.append(Game(num, max(reds), max(greens), max(blues)))
    return result


def part1(puzzle_input):
    s = sum(
        game.num
        for game in puzzle_input
        if game.red <= N_RED and game.green <= N_GREEN and game.blue <= N_BLUE
    )
    print(s)


def part2(puzzle_input):
    s = sum(game.red * game.green * game.blue for game in puzzle_input)
    print(s)


input = get_input(2023, 2)
puzzle_input = parse_input(input)

part1(puzzle_input[:])
part2(puzzle_input[:])
