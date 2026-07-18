from helpers.IDGenerator import IDGenerator
from helpers.vector import Vector
import math
id_gen = IDGenerator()

class Sphere:
    def __init__(self, x=0, y=0, z=0, r=1):
        self.origin = Vector(x, y, z)
        self.r = r
        self.id = id_gen.create(self.__class__)

    def intersect(self, ray):
        sphere_to_ray = ray.origin - self.origin

        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.r * self.r

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None

        sqrt_disc = math.sqrt(discriminant)

        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)

        hits = [t for t in (t1, t2) if t != 0]

        if not hits:
            return None
        #return hits for all point hits
        #return min(hits) for first hit point
        return hits
        