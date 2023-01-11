import json
from typing import Union, List
from .default import TempsDirectory

class Modeler:
    def __init__(self) -> None:
        self.temp_directory = TempsDirectory().temp_path
        
        self.temp_file_0d = "temp_0d_geometries"
        self.temp_file_1d = "temp_1d_geometries"
        self.temp_file_2d = "temp_2d_geometries"
        self.temp_file_3d = "temp_3d_geometries"
    
    """ 0D Primitive ============================================= """
    """ ========================================================== """

    def CreatePoint(
        self,
        points: List[float] = [0, 0, 0],
        size:  List[float] = [1, 1, 1],
        color: List[Union[int, str]] = "red",
        name: str = "Point"
    ):
        point = {
            "name": name,
            "points": points,
            "size": size,
            "color": color,
        }
        self.save_geometry(data=[point, point], file_name=self.temp_file_0d)
        return name


    """ 1D Primitive ============================================= """
    """ ========================================================== """

    def CreateLine(
        self,
        points: List[float] = [[0, 0, 0], [1, 1, 1]],
        color: List[Union[int, str]] = "red",
        name: str = "Line"
    ):
        return name
    
    def CreatePolyLine(
        self,
        points: List[float] = [[0, 0, 0], [1, 1, 1]],
        color: List[Union[int, str]] = "red",
        name: str = "Line"
    ):
        print(name)
    
    
    """ 2D Primitive ============================================= """
    """ ========================================================== """

    def CreateRectangular(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        size:  List[float] = [1, 1, 1],
        color: List[Union[int, str]] = "red",
        name: str = "Rectangular"
    ):
        print(name)
    
    def CreateCircle(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        radius: Union[float, str] = 1,
        color: List[Union[int, str]] = "red",
        name: str = "Circle"
    ):
        print(name)

    def CreateEllipse(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        semi_axes: Union[float, str] = 1,
        color: List[Union[int, str]] = "red",
        name: str = "Ellipse"
    ):
        print(name)

    
    def save_geometry(self, data, file_name):
        json_str = json.dumps(data)

        with open(str(self.temp_directory) +"/" + file_name + ".txt", 'w') as file:
            file.write(json_str)