import os, json
from typing import Union, List
from .default import TempsDirectory

class Modeler:
    def __init__(self) -> None:
        self.temp_directory = TempsDirectory().temp_path
        
        self.temp_file_0d = "temp_0d_geometries"
        self.temp_file_1d = "temp_1d_geometries"
        self.temp_file_2d = "temp_2d_geometries"
        self.temp_file_3d = "temp_3d_geometries"

        self.temp_list_0d = list()
        self.temp_list_1d = list()
        self.temp_list_2d = list()
        self.temp_list_3d = list()
    
    """ 0D Primitive ============================================= """
    """ ========================================================== """

    def CreatePoint(
        self,
        points: str = [0, 0, 0],
        size:  str = [1, 1, 1],
        name: str = "Point"
    ):
        parameters= {
            "name": name,
            "points": points,
            "size": size,
        }
        
        self.save_geometry(data=parameters, file_name=self.temp_file_0d)
        return name


    """ 1D Primitive ============================================= """
    """ ========================================================== """

    def CreateLine(
        self,
        points: List[float] = [[0, 0, 0], [1, 1, 1]],
        name: str = "Line"
    ):
        parameters= {
            "name": name,
            "points": points,
        }
        
        # print(self.l)
        self.save_geometry(data=parameters, file_name=self.temp_file_1d)
        return name
    
    def CreatePolyLine(
        self,
        points: List[float] = [[0, 0, 0], [1, 1, 1]],
        name: str = "Line"
    ):
        parameters= {
            "name": name,
            "points": points,
        }
        
        # print(self.l)
        self.save_geometry(data=parameters, file_name=self.temp_file_1d)
        return name
    
    
    """ 2D Primitive ============================================= """
    """ ========================================================== """

    def CreateRectangular(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        size:  List[float] = [1, 1, 1],
        name: str = "Rectangular"
    ):
        parameters = {
            "name": name,
            "center": center,
            "size": size
        }
        
        self.save_geometry(data=parameters, file_name=self.temp_file_2d)
        return name
    
    def CreateCircle(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        radius: Union[float, str] = 1,
        name: str = "Circle"
    ):
        parameters= {
            "name": name,
            "center": center,
            "radius": radius,
        }
        
        self.save_geometry(data=parameters, file_name=self.temp_file_2d)
        return name

    def CreateEllipse(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        semi_axes: Union[float, str] = 1,
        name: str = "Ellipse"
    ):
        parameters= {
            "name": name,
            "center": center,
            "semi_axes": semi_axes,
        }
        
        self.save_geometry(data=parameters, file_name=self.temp_file_2d)
        return name
    
    """ 3D Primitive ============================================= """
    """ ========================================================== """

    def CreateBox(
        self,
        center: List[float] = [[0, 0, 0], [1, 1, 1]],
        size:  List[float] = [1, 1, 1],
        name: str = "Box"
    ):
        parameters = {
            "name": name,
            "center": center,
            "size": size
        }

        self.save_geometry(data=parameters, file_name=self.temp_file_3d)
        return name

    """ Additional Function """
    def save_geometry(self, data, file_name):
        if file_name == self.temp_file_0d:
            self.temp_list_0d.append(data)
            self.save_as_json(self.temp_list_0d, file_name)
        
        elif file_name == self.temp_file_1d:
            self.temp_list_1d.append(data)
            self.save_as_json(self.temp_list_1d, file_name)

        elif file_name == self.temp_file_2d:
            self.temp_list_2d.append(data)
            self.save_as_json(self.temp_list_2d, file_name)
        
        elif file_name == self.temp_file_3d:
            self.temp_list_3d.append(data)
            self.save_as_json(self.temp_list_3d, file_name)
        
        else:
            raise IndexError


    def save_as_json(self, data, file_name):
        file_path = str(self.temp_directory / file_name) + ".json"
        with open(file_path, "w") as file:
            json.dump(data, file)