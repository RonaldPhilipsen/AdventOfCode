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
    """do the counting calories exercies
    """
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
