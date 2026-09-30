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


# ============================================================
# CANVAS
# ============================================================

width = 400
height = 400

canvas = [
    [[0, 0, 0] for _ in range(width)]
    for _ in range(height)
]


# ============================================================
# SPHERE
# ============================================================

s1 = Sphere(0, 0, 0, 1)

# IMPORTANT:
# This replaces the previous transform.
# s1.set_transform(
#     Transform.scaling(0.5, 2, 1)
# )

inverse = s1.transform.inverse()


# ============================================================
# MATERIAL
# ============================================================

s1.material = Material(
    Color(1, 1, 1),
    ambient=0.1,
    diffuse=0.9,
    specular=0.9,
    shininess=200
)


# ============================================================
# LIGHT
# ============================================================

light = PointLight(
    Point(-10, 10, -10),
    Color(1, 1, 1)
)


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
        direction = (pixel - camera).normalize()

        # Create ray
        ray = Ray(camera, direction)

        # Intersect sphere
        intersections = s1.intersect(
            ray,
            inverse
        )

        # Find closest visible intersection
        hit = intersections.hit()

        if hit is not None:

            # Find point where ray hit sphere
            point = ray.position(hit.t)

            # Find surface normal
            normal = s1.normal_at(point)

            # Eye vector points from hit point toward camera
            eyev = -ray.direction

            # Calculate lighting
            color = Lighting.lighting(
                s1.material,
                light,
                point,
                eyev,
                normal
            )

            # Convert Color 0-1+ → RGB 0-255
            r = max(0, min(1, color.r))
            g = max(0, min(1, color.g))
            b = max(0, min(1, color.b))

            canvas[y][x] = [
                round(r * 255),
                round(g * 255),
                round(b * 255)
            ]


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