# Import Library
import json, string, random


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


import random


def random_name(length = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_coordinate(number_point: int = 1):
    if number_point == 1:
        return [random.random() for _ in range(random.randint(1, 3))]
    else:
        return [[random.random() for _ in range(random.randint(1, 3))] for i in range(3)]


# print(random_coordinate(2))