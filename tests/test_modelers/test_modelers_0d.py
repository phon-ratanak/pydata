import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

# Import Library
import pytest
from maxwave.utils import random_coordinate, random_name, read_json
from maxwave import Modeler


modeler = Modeler()

temp_directory = modeler.temp_directory
temp_file_0d = modeler.temp_file_0d


""" Test for 0D """

point_0d_test = [(i, random_name(), random_coordinate()) for i in range(20)]
@pytest.mark.parametrize("index, name, points", point_0d_test)
def test_modeler_0d(index: int, name: str, points):
    modeler.CreatePoint(points=points, name=name)

    file_path = str(temp_directory / temp_file_0d) + ".json"
    data = read_json(file_path)

    assert data[index]["name"] == name
    assert data[index]["points"] == points

