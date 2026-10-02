from helpers.camera import Camera
import math
c = Camera.default_camera()

print(c.transform)


c2 = Camera(125,200,math.pi/2)

print(c2.pixel_size)