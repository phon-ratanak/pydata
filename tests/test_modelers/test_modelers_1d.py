import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

# Import Library
import pytest
import random
from maxwave.utils import random_coordinate, random_name, read_json
from maxwave import Modeler


modeler = Modeler()

temp_directory = modeler.temp_directory
temp_file_1d = modeler.temp_file_1d


""" Test for 1D  """
point_1d_line_test = [(i, random_name(), random_coordinate(random.randint(1, 10))) for i in range(20)]
@pytest.mark.parametrize("index, name, points", point_1d_line_test)
def test_modeler_1d(index, name, points):
    modeler.CreateLine(points=points, name=name)

    file_path = str(temp_directory/temp_file_1d) + ".json"
    data = read_json(file_path)

    assert data[index]["name"] == name
    assert data[index]["points"] == points





