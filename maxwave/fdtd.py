from .desktop import Desktop

class FDTD(Desktop):
    def __init__(
        self,
        simulation_type: str = "FDTD",
        project_name: str = "PMaxwave",
        project_path: str = None
    ) -> None:
    
        super().__init__(simulation_type, project_name, project_path)
