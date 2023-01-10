from .desktop import Desktop

class FDTD(Desktop):
    def __init__(
        self, 
        project_name: str = "PMaxwave", 
        simulation_type: str = "FDTD"
    ) -> None:
    
        super().__init__(project_name, simulation_type)