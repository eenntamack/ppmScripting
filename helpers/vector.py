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