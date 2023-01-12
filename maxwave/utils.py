import json
import string
import random


def read_json(file_path: str) -> dict:
    """Reads a JSON file located at the specified file_path and returns
    its content as a python object

    Args:
    file_path: str:  path of the file

    Returns:
    dict : return file content as a python object
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'Error: {file_path} not found')
    except json.decoder.JSONDecodeError:
        print(f'Error: {file_path} is empty')


def random_name(length: int = 10) -> str:
    """return a random string that consists of letters and digits with length

    Args:
    length: int : length of the returned string. default is 10

    Returns:
    str : random generated string
    """
    name = ''.join(random.choices(
            string.ascii_letters + string.digits, k=length
            ))

    return name


def random_coordinate(number_points: int = 1):
    """returns a list of `number_points` lists, each of which contains
        3 random float numbers representing x, y, and z coordinates.

    Args:
    number_points: int : number of coordinates need to be generated

    Returns:

    """
    point = [
        [
            random.uniform(-90, 90),
            random.uniform(-180, 180),
            random.uniform(-90, 90)
        ] for i in range(number_points)]
    return point
