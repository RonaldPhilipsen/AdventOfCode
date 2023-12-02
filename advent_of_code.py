from pathlib import PosixPath
import requests
import os

INPUT_PATH = PosixPath(os.getcwd(),'input')
HTTP_OK = 200


def download_input(year: int, day: int) -> str:
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

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    request = requests.Request('GET',  url, headers={
                               'Cookie': f'session={cookie}'})
    prepared_request = request.prepare()

    session = requests.Session()
    result = session.send(prepared_request, timeout=100)

    if result.status_code != HTTP_OK:
        raise Exception(
            f'failed to get input for {year}/{day}, status code {result.status_code}')

    return result.text


def get_input(year: int, day: int):
    yeardir = INPUT_PATH.joinpath(str(year))
    yeardir.mkdir(parents=True, exist_ok=True)


    if f'{day}_input.txt' in os.listdir(yeardir):
        with open(f'{yeardir.as_posix()}/{day}_input.txt', 'r', encoding='UTF-8') as f:
            return f.read()
    else:
        txt = download_input(year=year, day=day)
        with open(f'{yeardir.as_posix()}/{day}_input.txt', 'w', encoding='UTF-8') as f:
            f.write(txt)
        return txt
