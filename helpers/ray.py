
import math
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def position(self, t):
        return self.origin + self.direction * t
    def transform(self, matrix):
        org = self.origin.tmulm(matrix.inverse()) #.inverse()
        dir = self.direction.tmulm(matrix.inverse())
        return Ray(org, dir)
    def print(self):
        print("Origin: ")
        self.origin.print()
        print("Direction")
        self.direction.print()
