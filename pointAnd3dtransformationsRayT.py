from helpers.point import Point
from helpers.transformations import Transform as t
import math

width, height = 1000, 1000
canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]

center_x = width // 2
center_y = height // 2
scale = 80

points = []

numPoints = 100
# build circle in XY plane
for i in range(numPoints):
    theta = 2 * math.pi * i / numPoints
    x = math.cos(theta) * 5
    y = math.sin(theta) * 5
    z = 0
    points.append(Point(x, y, z))

rot = t.rotation_x(math.radians(30)) * t.rotation_y(math.radians(30))

def draw_point(canvas, x, y, color, radius=2):
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            if dx*dx + dy*dy <= radius*radius:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    canvas[ny][nx] = color

# IMPORTANT FIX HERE
for p in points:
    p2 = rot * p   # rotate

    x = int(center_x + p2.x * scale)
    y = int(center_y + p2.y * scale)

    draw_point(canvas, x, y, [200, 0, 0], 5)



with open("ppmStudy.ppm", "w") as f:
    f.write(f"P3\n{width} {height}\n255\n")
    for row in canvas:
        for r, g, b in row:
            f.write(f"{r} {g} {b} ")
        f.write("\n")
# write ppm
# total_frames = 30

# for frame in range(total_frames):
#     canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
#     filename = f"ray_frame_{frame:02d}.ppm"
#     rot = (
#         t.rotation_x(math.radians(30 + frame * 5)) *
#         t.rotation_y(math.radians(30 + frame * 10))
#     )

#     for p in points:
#         p2 = rot * p
#         x = int(center_x + p2.x * scale)
#         y = int(center_y + p2.y * scale)
#         draw_point(canvas, x, y, [200, 0, 0], radius=2)

#     with open(filename, "w") as f:
#         f.write(f"P3\n{width} {height}\n255\n")
#         for row in canvas:
#             for r, g, b in row:
#                 f.write(f"{r} {g} {b} ")
#             f.write("\n")