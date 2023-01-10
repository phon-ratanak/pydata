from typing import Union, List

class Modeler:
    def __init__(self) -> None:
      pass
    
    """ 0D Primitive ============================================= """
    """ ========================================================== """

    def CreatePoint(
        self,
        points: List[float] = [0, 0, 0],
        size:  List[float] = [1, 1, 1],
        color: List[Union[int, str]] = "red",
        name: str = "Point"
    ):
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

    

