import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

# Import Library
from maxwave import Modeler



def test_modeler():
    modeler = Modeler()

    assert modeler.CreateLine() == "Line"


# test_modeler()