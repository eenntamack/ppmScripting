from helpers.IDGenerator import IDGenerator
from helpers.vector import Vector
from helpers.ray import Ray
from helpers.threedoperations import Intersection
from helpers.threedoperations import Intersections
import math
id_gen = IDGenerator()

class Sphere:
    def __init__(self, x=0, y=0, z=0, r=1):
        self.origin = Vector(x, y, z)
        self.r = r
        self.id = id_gen.create(self.__class__)
        self.intersections = []

    def intersect(self, ray: Ray):

        object_to_ray = ray.origin - self.origin

        a = ray.direction.dot(ray.direction)

        b = 2 * ray.direction.dot(object_to_ray)

        c = object_to_ray.dot(object_to_ray) - self.r ** 2

        discriminant = b * b - 4 * a * c

        if discriminant < 0:

            return Intersections()

        sqrt_disc = math.sqrt(discriminant)

        t1 = (-b - sqrt_disc) / (2 * a)

        t2 = (-b + sqrt_disc) / (2 * a)

        return Intersections(

            Intersection(t1, self),

            Intersection(t2, self)

        )
    def __str__(self):
        return self.id
    def __repr__(self):
            return f"Sphere('{self.id}')"
        