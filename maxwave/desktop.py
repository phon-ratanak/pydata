import os, pathlib
from .modelers import Modeler

class Desktop:
    def __init__(
        self,
        project_name: str = "PMaxwave",
        simulation_type: str = "FDTD"
    ):

        self.project_name = project_name
        self.create_directory()

        self.list_0d_objects = []
        self.list_1d_objects = []
        self.list_2d_objects = []
        self.list_3d_objects = []

        self.modeler = Modeler()

    
    def create_directory(self):
        """
        Create the default directory for storing simulation datas.

        Returns:
            List[pathlib.Path]: list of all the directories created
        """
        home = pathlib.Path.home()
        simulation_path = home / "Documents" / "MaxWave" / self.project_name
        dirs_to_create = [
            simulation_path / "info",
            simulation_path / "data",
            simulation_path / "images",
            simulation_path / "animations",
            simulation_path / "geometries",
        ]
        [path.mkdir(parents=True, exist_ok=True) for path in dirs_to_create]
        return dirs_to_create
