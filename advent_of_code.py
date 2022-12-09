import requests
import os

INPUT_PATH = os.getcwd() + '/input'
HTTP_OK = 200

def download_input(day: int) -> str:
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


def get_input(day: int):
    try:
        os.stat(INPUT_PATH)
    except FileNotFoundError:
        os.mkdir(INPUT_PATH)

    if f'{day}_input.txt' in os.listdir(INPUT_PATH):
        with open(f'{INPUT_PATH}/{day}_input.txt', 'r', encoding='UTF-8') as f:
            return f.read()
    else:
        txt = download_input(day)
        with open(f'{INPUT_PATH}/{day}_input.txt', 'w', encoding='UTF-8') as f:
            f.write(txt)
        return txt
