from helpers.ray import Ray
from helpers.point import Point
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.threedoperations import Intersection
from helpers.transformations import Transform
origin = Point(0,1,0)
direction = Vector(0,0,1)

r = Ray(origin, direction)

p =r.position(4)

p.print()

s1 = Sphere(0,0,0,1)
s2 = Sphere()

print(s1.id)
print(s2.id)

i = Intersection(s1.intersect(r),s1)
print(i.t)


print("First R")
r.print()
m = Transform.scaling(2,5,5)
m2 = Transform.translation(5,4,3)

r2 = r.transform(m)

print("Newly transformed R")
r2.print()


r3 = r.transform(m2)
print("Translated R")
r3.print()