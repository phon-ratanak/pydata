import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

# Import Library
from maxwave import FDTD
from tqdm import tqdm

fdtd = FDTD(
        simulation_type="FDTD",
        project_name="PMaxwave2",
        # project_path="C:/Users/Ratanak/Documents/MaxWave/ere"
)
fdtd.modeler.CreatePoint(points=[1,1,1], name="Point1")
fdtd.modeler.CreatePoint(points=[2.1,0.1,3], name="Point2")
fdtd.modeler.CreateLine(points=[[1,1,1], [1,0,1]], name="Line1")
fdtd.modeler.CreateLine(points=[[0,0,1], [0,0,1]], name="Line1")



fdtd.Validation()
# print(fdtd.project_path)
# fdtd.Simulation()


