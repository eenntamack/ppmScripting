import math

from helpers.ray import Ray
from helpers.point import Point
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.transformations import Transform


# ============================================================
# CANVAS
# ============================================================

width = 200
height = 200

canvas = [
    [[0, 0, 0] for _ in range(width)]
    for _ in range(height)
]


# ============================================================
# SPHERE
# ============================================================

s1 = Sphere(0, 0, 0, 1)

# Put sphere directly in front of camera
s1.set_transform(
    Transform.translation(0, 0, 3)
)

inverse = s1.transform.inverse()

print("SPHERE TRANSFORM:")
print(s1.transform)

print("\nINVERSE:")
print(inverse)


# ============================================================
# CAMERA
# ============================================================

camera = Point(0, 0, -5)

wall_z = 0
wall_size = 4

pixel_size = wall_size / width
half = wall_size / 2


# ============================================================
# RAY CASTING
# ============================================================

print("\nRendering...")

for y in range(height):

    world_y = half - pixel_size * y

    for x in range(width):

        world_x = -half + pixel_size * x

        pixel = Point(
            world_x,
            world_y,
            wall_z
        )

        # Camera → pixel
        direction = pixel - camera

        # Normalize
        direction = direction.normalize()

        # Create ray
        ray = Ray(
            camera,
            direction
        )

        # IMPORTANT:
        # Pass the already-calculated inverse.
        intersections = s1.intersect(
            ray,
            inverse
        )

        hit = intersections.hit()

        if hit is not None:
            canvas[y][x] = [200, min(math.floor(0 + x/5) ,255), 0]
        if x == width // 2 and y == height // 2:

            print("CENTER RAY")
            print("origin:", ray.origin)
            print("direction:", ray.direction)

            test_intersections = s1.intersect(ray, inverse)

            print("intersections:", test_intersections)
            print("count:", test_intersections.count)

            for intersection in test_intersections.inters:
                print("t =", intersection.t)

            print("hit:", test_intersections.hit())


# ============================================================
# WRITE PPM
# ============================================================

filename = "sphere.ppm"

with open(filename, "w") as f:

    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")

    for row in canvas:

        for r, g, b in row:
            f.write(f"{r} {g} {b} ")

        f.write("\n")


print(f"\nRendered sphere to {filename}")