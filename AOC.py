"""Script to do AOC in python

Raises:
    Exception: If we fail to load the cookie
    Exception: if we fail to get a HTTP_OK

Returns:
    int: 0 on OK or 1 on NOK
"""
from typing import List
from functools import cache
import requests

HTTP_OK = 200


@cache
def get_input(day: int) -> str:
    """gets the input for a given day of AOC

    Args:
        day (int): the day that we want the input for

    Raises:
        Exception: If we fail to load the cookie
        Exception: if we fail to get a HTTP_OK

    Returns:
        str: the input as a plain text string
    """
    with open('.cookie', 'r', encoding='UTF-8') as f:
        cookie = f.readline().strip('\n')

    if not cookie:
        raise Exception('failed to read cookie data')

    url = f'https://adventofcode.com/2022/day/{day}/input'
    request = requests.Request('GET',  url, headers={
                               'Cookie': f'session={cookie}'})
    prepared_request = request.prepare()

    session = requests.Session()
    result = session.send(prepared_request, timeout=100)

    if result.status_code != HTTP_OK:
        raise Exception(
            f'failed to get input for day {day}, status code {result.status_code}')

    return result.text


def do_day_1():
    """do the counting calories exercise """
    input_str = get_input(1)
    input_list = input_str.split('\n')
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

    print(f'max_calories: {total_calories[0]}')
    print(f'top 3 calories: {sum(total_calories[0:3])}')


def do_day_2():
    """do the rock_paper scissors exercise """
    I_ROCK = 'A'
    I_PAPER = 'B'
    I_SCISSORS = 'C'

    O_ROCK_LOSE = 'X'
    O_PAPER_DRAW = 'Y'
    O_SCISSORS_WIN = 'Z'

    SCORE_ROCK = 1
    SCORE_PAPER = 2
    SCORE_SCISSORS = 3

    LOSS = 0
    DRAW = 3
    WIN = 6

    scores_map = {
        f'{I_ROCK} {O_ROCK_LOSE}': [(SCORE_ROCK + DRAW), (SCORE_SCISSORS + LOSS)],
        f'{I_ROCK} {O_PAPER_DRAW}': [(SCORE_PAPER + WIN), (SCORE_ROCK + DRAW)],
        f'{I_ROCK} {O_SCISSORS_WIN}': [(SCORE_SCISSORS + LOSS), (SCORE_PAPER + WIN)],
        f'{I_PAPER} {O_ROCK_LOSE}': [(SCORE_ROCK + LOSS), (SCORE_ROCK + LOSS)],
        f'{I_PAPER} {O_PAPER_DRAW}': [(SCORE_PAPER + DRAW), (SCORE_PAPER + DRAW)],
        f'{I_PAPER} {O_SCISSORS_WIN}': [(SCORE_SCISSORS + WIN), (SCORE_SCISSORS + WIN)],
        f'{I_SCISSORS} {O_ROCK_LOSE}': [(SCORE_ROCK + WIN), (SCORE_PAPER + LOSS)],
        f'{I_SCISSORS} {O_PAPER_DRAW}': [(SCORE_PAPER + LOSS), (SCORE_SCISSORS + DRAW)],
        f'{I_SCISSORS} {O_SCISSORS_WIN}': [(SCORE_SCISSORS + DRAW), (SCORE_ROCK + WIN)],
    }

    input_str = get_input(2)
    input_list = input_str.split('\n')

    scores_part1 = [scores_map[i][0] for i in input_list if i]
    scores_part2 = [scores_map[i][1] for i in input_list if i]
    print(f'Total: {sum(scores_part1)}')
    print(f'Total: {sum(scores_part2)}')
