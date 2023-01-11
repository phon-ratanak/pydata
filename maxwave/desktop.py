import shutil

from .default import Directory, ProjectDirectory
from .modelers import Modeler


class Desktop:
    def __init__(
        self,
        simulation_type: str = "FDTD",
        project_name: str = "PMaxwave",
        project_path: str = None
    ):
        self.project_name = project_name
        self.simulation_type = simulation_type

        if project_path is not None:
            self.project_path = project_path 
        else:
            self.project_path = Directory().default_path

    
        self.modeler = Modeler()
        self.temp_directory = self.modeler.temp_directory
    

    
    def Validation(self):
        """
        This function validates the project directory and copies the files 
        from the temp directory to the project's geometry directory.
        """
        self.project_path = ProjectDirectory(
            project_path=self.project_path, 
            project_name=self.project_name        
        ).default_path

        # Copy geometry data from temp to geometry directory.
        shutil.copytree(
            self.temp_directory,
            self.project_path / self.project_name / "geometry", 
            dirs_exist_ok=True
        )
        # Delete temp directory.
        shutil.rmtree(self.temp_directory)
    
        
    def Simulation(self):
        pass

    

