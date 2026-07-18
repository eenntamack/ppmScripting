
from helpers.vector4 import Tuple

class Point(Tuple):
    def __init__(self, x, y, z, w=1):
        super().__init__(x, y, z, w)