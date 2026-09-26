import math
from helpers.ray import Ray
from helpers.matrix import Matrix



class Ray_OP:
    @staticmethod
    def transform(r : Ray, m : Matrix ):
        origin = r.origin.tmulm(m)
        direction = r.direction.tmulm(m)
        return Ray(origin, direction)