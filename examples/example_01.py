import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

# Import Library
from maxwave import FDTD

fdtd = FDTD(
        simulation_type="FDTD",
        project_name="PMaxwave",
        # project_path="C:/Users/Ratanak/Documents/MaxWave/ere"
)

fdtd.modeler.CreatePoint()
# fdtd.modeler.CreatePoint()
# fdtd.modeler.CreateLine()
# fdtd.modeler.CreateRectangular()
# fdtd.

# print(fdtd.list_0d_objects)
# fdtd.CreatePoint()


fdtd.Validation()
print(fdtd.project_path)
# fdtd.Simulation()