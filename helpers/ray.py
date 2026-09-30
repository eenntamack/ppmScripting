
import math
from helpers.point import Point
from helpers.vector import Vector
from helpers.matrix import Matrix
class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin
        self.direction = direction #.normalize()

    def position(self, t: float) -> Point:
        return self.origin + self.direction * t
    def transform(self, matrix: Matrix):
        org = self.origin.tmulm(matrix.inverse()) #.inverse()
        dir = self.direction.tmulm(matrix.inverse())
        return Ray(org, dir)
    def print(self):
        print("Origin: ")
        self.origin.print()
        print("Direction")
        self.direction.print()
    def __neg__(self):
        return Ray(self.origin,-self.direction)
