from helpers.ray import Ray
from helpers.point import Point
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.threedoperations import Intersection
from helpers.threedoperations import Intersections
from helpers.transformations import Transform
from helpers.ray_functions import Ray_OP
from helpers.color import Color
from helpers.lights import PointLight
from helpers.material import Material
from helpers.lighting import Lighting

import math
origin = Point(1,2,-2)
direction = Vector(0,0,1)

r = Ray(origin, direction)

s1 = Sphere(0,0,0,1)
s1.set_transform(Transform.translation(0,1,0))

n = s1.normal_at(Point(0,1.70711,-0.70711))


print(f"the normal at (0,0,1) {n}")


print("reflection test: ")
v = Vector(0,-1,0)
norm = Vector(math.sqrt(2)/2,math.sqrt(2)/2,0)
refl = Ray_OP.reflect(v,norm)

print(refl)


pl = PointLight(Vector(0,0,0),Color())
print(pl)
print(pl.intensity)
print(pl.position)

print(s1.material)

newMat = Material(Color(1,1,1),0.1,0.9,0.9,200)
s1.material = newMat
print(s1.material)

lighting = Lighting.lighting(newMat,PointLight(Vector(0,0,-10),Color(1,1,1)),Vector(0,0,0),Vector(0,0,-1),Vector(0,0,-1))

print("Lighting: ",lighting)