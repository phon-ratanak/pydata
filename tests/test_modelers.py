import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

# Import Library
import pytest
import json, string, random
from maxwave import Modeler

""" Function ==============="""
def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


import random

alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]


def random_name(length = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_coor():
    return [random.random() for _ in range(random.randint(1, 3))]
""" ======================= """


modeler = Modeler()

temp_directory = modeler.temp_directory

temp_file_0d = modeler.temp_file_0d
temp_file_1d = modeler.temp_file_1d
temp_file_2d = modeler.temp_file_2d
temp_file_3d = modeler.temp_file_3d

point_0d_test = [(i, random_name(), random_coor()) for i in range(100)]
print(point_0d_test)
@pytest.mark.parametrize("index, name, points", point_0d_test)
def test_modeler_0d(index, name, points):
    modeler.CreatePoint(points=points, name=name)

    file_path = str(temp_directory/temp_file_0d) + ".json"
    data = read_json(file_path)

    assert data[index]["name"] == name
    assert data[index]["points"] == points


# test_modeler()


