from helpers.vector4 import Tuple
class Vector(Tuple):
    def __init__(self, x, y, z, w=0):
        super().__init__(x, y, z, w)

    def magnitude(self):
        return (self.x**2 +
                self.y**2 +
                self.z**2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        return Vector(
            self.x / mag,
            self.y / mag,
            self.z / mag
        )
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def __neg__(self):
        return Vector(
            -self.x,
            -self.y,
            -self.z
        )
    def cross(self,other):
            return Vector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * self.y - self.y * other.x
            )
    def __sub__(self,other):
            return self.__class__(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z,
            )