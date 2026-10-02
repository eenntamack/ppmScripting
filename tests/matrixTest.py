import helpers.matrix as m
import random

a = m.Matrix(4,4)
b = m.Matrix(4,4)

for _ in range(12):
    a.setRandomPoints(random.randint(2,5))
    b.setRandomPoints(random.randint(2,5))


print("____a____")
a.print()

print("____b____")
b.print()

C = a * b
B_inv = b.inverse()

result = C * B_inv
print("result_____>")
result.print()

print(a == b)

print("______________")

print("TEST: (A * B) * B^-1 == A")
I = b * b.inverse()
I.print()
print("______________")
print("")
print(a._poinData(2,1))


print("ORIGINAL MATRIX")
a.print()

print("\nTRANSPOSE")
t = a.transpose()
t.print()

print("\nSUBMATRIX (0,0)")
sub = a.submatrix(0,0)
sub.print()

print("\n2x2 determinant from sub-submatrix")
sub2 = sub.submatrix(0,0)
print(sub2.determinant())

print("\n3x3 determinant")
print(sub.determinant())

print("\n4x4 determinant (original)")
print(a.determinant())

print("\nINVERSE")
inv = a.inverse()
inv.print()

