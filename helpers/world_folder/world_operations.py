from helpers.world import World
from helpers.ray import Ray
from helpers.threedoperations import Intersections
from helpers.threedoperations import Intersection
from helpers.vector import Vector
from helpers.lighting import Lighting
from helpers.color import Color
class World_OPS:
    @staticmethod
    def intersect_world(world: World, ray: Ray):
        inters = []

        for item in world.objects:
            intersections = item.intersect(ray)
            inters.extend(intersections.inters)

        inters.sort(key=lambda i: i.t)

        return Intersections(*inters)
    
class Computations:
    def __init__(self, t, object, point, eyev, normalv: Vector):
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev
        self.inside = normalv.dot(eyev) < 0

        if self.inside:
            normalv = -normalv
        self.normalv = normalv

    @staticmethod
    def prepare_computations(intersection: Intersection, ray: Ray):
        point = ray.position(intersection.t)

        return Computations(
            intersection.t,
            intersection.object,
            point,
            -ray.direction,
            intersection.object.normal_at(point)
        )
    def shade_hit(self, w: World):
        print("material color:", self.object.material.color)

        print("ambient:", self.object.material.ambient)

        print("diffuse:", self.object.material.diffuse)

        print("specular:", self.object.material.specular)
            
        return Lighting.lighting(
            self.object.material,
            w.lights[0],
            self.point,
            self.eyev,
            self.normalv
        )

class ColorPixel:
    @staticmethod
    def color_at(w: World, r: Ray):
        xs = World_OPS.intersect_world(w, r)

        hit = xs.hit()

        if hit is None:
            return Color(0, 0, 0)

        comps = Computations.prepare_computations(hit, r)

        return comps.shade_hit(w)