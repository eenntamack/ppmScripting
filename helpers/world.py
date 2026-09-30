from helpers.lights import PointLight
from helpers.shapes import Sphere
from helpers.color import Color
from helpers.transformations import Transform
from helpers.point import Point

class World:
    def __init__(self, objects=None, lights=None):
        self.objects = [] if objects is None else list(objects)
        self.lights = [] if lights is None else list(lights)

    @classmethod
    def default_world(cls):
        light = PointLight(
            Point(-10, 10, -10),
            Color(1, 1, 1)
        )

        s1 = Sphere()
        s1.material.color = Color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2

        s2 = Sphere()
        s2.set_transform(
            Transform.scaling(0.5, 0.5, 0.5)
        )

        return cls(
            objects=[s1, s2],
            lights=[light]
        )
    