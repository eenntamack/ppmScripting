from helpers.ray import Ray
from helpers.point import Point
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.threedoperations import Intersection
from helpers.threedoperations import Intersections
from helpers.transformations import Transform
origin = Point(0,0,0)
direction = Vector(0,0,1)

r = Ray(origin, direction)

s1 = Sphere(0,0,0,1)
s2 = Sphere()
#
i = Intersection(1,s1)
print(i.t)

i2 = Intersection(2,s2)

iList = Intersections(i,i2)

iList.add_intersect(Intersection(-3,s2))

print(f"total intersections: {iList.count}")
print(f"intersection at ray 1 {iList[0].object}")
print(f"intersection at ray 2 {iList[1].t}")

print(iList.hit())