from helpers.point import Point
from helpers.transformations import Transform as t


p = Point(3,2,3)
transl = t.translation(1,9,2)

c = transl * p

print("old p")
p.print()
transl.print()
print("c")
c.print()

print("new p")
p = transl * p
p.print()



scl = t.scaling(1,2,3)

p = scl * p

print("scaling")
scl.print()

print("scaledP")
p.print()


reflX = t.reflection(x=True)
print("reflect X")


p = reflX * p
print("reflect X of p")
p.print()