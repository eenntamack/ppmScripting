import math

from helpers.ray import Ray
from helpers.point import Point
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.transformations import Transform
from helpers.color import Color
from helpers.lights import PointLight
from helpers.lighting import Lighting
from helpers.material import Material
from helpers.world import World
from helpers.world_folder.world_operations import World_OPS
from helpers.ray_functions import Ray_OP
from helpers.world_folder.world_operations import Computations
from helpers.threedoperations import Intersection
from helpers.world_folder.world_operations import ColorPixel

world = World.default_world()

r = Ray(
    Point(0, 0, -5),
    Vector(0, 0, 1)
)

# s1 = world.objects[0]
# i = Intersection(4, s1)

# comp = Computations.prepare_computations(i, r)

# print(comp.inside)

# c = comp.shade_hit(world)

c = ColorPixel.color_at(world,r)
print(c)