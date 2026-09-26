
from helpers.vector4 import Tuple
from helpers.vector import Vector

class Point(Tuple):
    def __init__(self, x, y, z, w=1):
        super().__init__(x, y, z, w)
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )