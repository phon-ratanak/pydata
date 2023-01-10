import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

# Import Library
from maxwave import FDTD

fdtd = FDTD(
    project_name="UnitCell", 
    simulation_type="FDTD"
)

fdtd.modeler.CreatePoint()
fdtd.modeler.CreateLine()
fdtd.modeler.CreateRectangular()
fdtd.modeler.CreateCircle()

