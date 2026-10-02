from helpers.world import World
from helpers.camera import Camera
from helpers.renderer import Render
from helpers.lights import PointLight
from helpers.vector import Vector
from helpers.shapes import Sphere
from helpers.camera_folder.camera_operations import Cam_OPS
from helpers.color import Color
from helpers.material import Material
from helpers.transformations import Transform
from helpers.point import Point
import math
width = 200
height = 200

floor = Sphere()
floor.set_transform(Transform.scaling(10,0.01,10))
floor.material = Material()
floor.material.color = Color(1,0.9,0.9)
floor.material.specular = 0
floor.material.ambient = 0.5

left_wall = Sphere()
left_wall.set_transform(
    Transform.translation(0,0,5)*
    Transform.rotation_y(-math.pi/4) * Transform.rotation_x(math.pi/2) *
    Transform.scaling(10,0.01,10)
)
left_wall.material = Material()
left_wall.material.color = Color(0.5,0.9,0.9)
left_wall.material.ambient = 0.5

right_wall = Sphere()
right_wall.set_transform(
    Transform.translation(0,0,5)*
    Transform.rotation_y(math.pi/4) * Transform.rotation_x(math.pi/2) *
    Transform.scaling(10,0.01,10)
)
right_wall.material = Material()
right_wall.material.color = Color(1,0.9,0.2)
right_wall.material.ambient = 0.5

large_sphere = Sphere()
large_sphere.set_transform(Transform.translation(-0.5,1,0.5))
large_sphere.material = Material()
large_sphere.material.color = Color(0.1,1,0.5)
large_sphere.material.diffuse = 0.7
large_sphere.material.specular = 0.3

small_sphere = Sphere()
small_sphere.set_transform(Transform.translation(1.5,0.5,-0.5)*Transform.scaling(0.5,0.5,0.5))
small_sphere.material = Material()
small_sphere.material.color = Color(0.1,1,0.5)
small_sphere.material.diffuse = 0.7
small_sphere.material.specular = 0.3

smallest_sphere = Sphere()
smallest_sphere.set_transform(Transform.translation(-1.5,0.33,-0.75) * Transform.scaling(0.33,0.33,0.33))
smallest_sphere.material = Material()
smallest_sphere.material.color = Color(1,0.8,0.1)
smallest_sphere.material.diffuse = 0.7
smallest_sphere.material.specular = 0.3
light = PointLight(Point(-10,10,-10),Color(1,1,1))

world = World([large_sphere,small_sphere,smallest_sphere,left_wall,floor,right_wall],[light])


camera = Camera(width,height,math.pi/3)


camera.transform = Cam_OPS.view_transform(
    Point(0,1.5,-5),
    Point(0,1,0),
    Vector(0,1,0)   
)


canvas = Render.render(camera,world)
filename = "sphere.ppm"

with open(filename, "w") as f:

    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")

    for row in canvas:
        for r, g, b in row:
            f.write(f"{r} {g} {b} ")

        f.write("\n")
