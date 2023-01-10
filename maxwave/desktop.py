import os, pathlib
from .modelers import Modeler

class Desktop:
    def __init__(
        self,
        project_name: str = "PMaxwave",
        simulation_type: str = "FDTD"
    ) -> None:

        self.create_directory()
        self.modeler = Modeler()

    def create_directory(self):
        """
        Create the default directory for storing simulation datas.

        Returns:
            str: The path to the default directory.
        """
        home = pathlib.Path.home()
        path = home / "Documents" / "MaxWave"

        os.makedirs(path, exist_ok=True)
        return str(path)

