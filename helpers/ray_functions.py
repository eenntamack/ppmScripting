import math
from helpers.ray import Ray
from helpers.matrix import Matrix

EPSILON = 1e-5

def approx_equal(a, b, epsilon=EPSILON):
    return abs(a - b) < epsilon

def clean_float(x, epsilon=1e-10):
    if abs(x) < epsilon:
        return 0.0
    return x

class Ray_OP:
    @staticmethod
    def transform(r : Ray, m : Matrix ):
        origin = r.origin.tmulm(m)
        direction = r.direction.tmulm(m)
        return Ray(origin, direction)
    @staticmethod
    def reflect(vector, normal):
        return vector - normal * 2 * vector.dot(normal)