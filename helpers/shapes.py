from helpers.IDGenerator import IDGenerator
from helpers.vector import Vector
from helpers.ray import Ray
from helpers.threedoperations import Intersection
from helpers.threedoperations import Intersections
from helpers.transformations import Transform
from helpers.ray_functions import Ray_OP
from helpers.material import Material

import math

id_gen = IDGenerator()

class Shape:
    pass
class Sphere(Shape):
    def __init__(self, x=0, y=0, z=0, r=1, material:Material = Material()):
        self.origin = Vector(x, y, z)
        self.r = r
        self.id = id_gen.create(self.__class__)
        self.intersections = []
        self.transform = Transform.identity()
        self.material = material

    def intersect(self, ray: Ray, inverse_transform=None):

        if inverse_transform is None:
            inverse_transform = self.transform.inverse()

        ray = Ray_OP.transform(ray, inverse_transform)

        # print("OBJECT RAY")
        # print("origin:", ray.origin)
        # print("direction:", ray.direction)

        # object_to_ray = ray.origin - self.origin
        object_to_ray = ray.origin

        # print("object_to_ray:", object_to_ray)

        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(object_to_ray)
        c = object_to_ray.dot(object_to_ray) - self.r ** 2

        # print("a:", a)
        # print("b:", b)
        # print("c:", c)

        discriminant = b * b - 4 * a * c

        # print("discriminant:", discriminant)

        if discriminant < 0:
            return Intersections()

        sqrt_disc = math.sqrt(discriminant)

        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)

        # print("t1:", t1)
        # print("t2:", t2)

        return Intersections(
            Intersection(t1, self),
            Intersection(t2, self)
        )
    
    def set_transform(self, transformation):
         self.transform = transformation
         
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return f"Sphere('{self.id}')"

    def normal_at(self, point):
        inverse = self.transform.inverse()

        object_point = point.tmulm(inverse)

        object_normal = object_point - self.origin

        world_normal = object_normal.tmulm(
            inverse.transpose()
        )

        return world_normal.normalize()
    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, Material):
            raise TypeError("color must be a Color")
        self._material = value