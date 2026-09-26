from helpers.ray import Ray
from helpers.point import Point
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.threedoperations import Intersection
from helpers.threedoperations import Intersections
from helpers.transformations import Transform
from helpers.ray_functions import Ray_OP

import math
origin = Point(1,2,-2)
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


#Translating a ray
new_ray_t = Ray_OP.transform(r,Transform.translation(2,1,2))

print("Translating a ray")
print("translation factor (2,1,2)")
print(f"old origin of r : {r.origin} , old direction of r : {r.direction} | \n new origin of r : {new_ray_t.origin} , new direction of r : {new_ray_t.direction}")

#Scaling a ray

new_ray_s = Ray_OP.transform(r,Transform.scaling(2,1,4))
print("Scaling a ray")
print("Scaling factor (2,1,4)")
print(f"old origin of r : {r.origin} , old direction of r : {r.direction} | \n new origin of r : {new_ray_s.origin} , new direction of r : {new_ray_s.direction}")

#Rotating a ray
new_ray_r = Ray_OP.transform(r,Transform.rotation_z(math.pi/2))
print("Rotating a ray")
print("Rotating factor pi")
print(f"old origin of r : {r.origin} , old direction of r : {r.direction} | \n new origin of r : {new_ray_r.origin} , new direction of r : {new_ray_r.direction}")

#transforming the sphere's transform

print("changing sphere's transform")
print(f"before {s1.transform}")
s1.set_transform(Transform.translation(1,2,1))
print(f"after {s1.transform}")


print(f"intersection: {s1.intersect(r)}")
xs = s1.intersect(r)
print(f"counts {xs.count}, all t: {xs[0].t}")