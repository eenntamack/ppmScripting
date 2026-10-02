from helpers.vector import Vector
from helpers.matrix import Matrix
from helpers.transformations import Transform
from helpers.camera import Camera
from helpers.ray import Ray
from helpers.point import Point
class Cam_OPS:
    @staticmethod
    def view_transform(_from, _to, _up):
        forward = (_to - _from).normalize()
        upn = _up.normalize()

        left = forward.cross(upn)
        true_up = left.cross(forward)

        orientation = Matrix(4, 4)

        orientation[0][0] = left.x
        orientation[0][1] = left.y
        orientation[0][2] = left.z
        orientation[0][3] = 0

        orientation[1][0] = true_up.x
        orientation[1][1] = true_up.y
        orientation[1][2] = true_up.z
        orientation[1][3] = 0

        orientation[2][0] = -forward.x
        orientation[2][1] = -forward.y
        orientation[2][2] = -forward.z
        orientation[2][3] = 0

        orientation[3][0] = 0
        orientation[3][1] = 0
        orientation[3][2] = 0
        orientation[3][3] = 1

        return orientation * Transform.translation(
            -_from.x,
            -_from.y,
            -_from.z
        )
    @staticmethod
    def ray_for_pixel(camera: Camera,px: int | float, py: int | float):
        # the offset from the edge of the canvas to the pixel's center
        xoffset = (px + 0.5) * camera.pixel_size
        yoffset = (py + 0.5) * camera.pixel_size

        # the untransformed coordinates of the pixel in world space 
        # (remember that the camera looks towards -z, so +x is to the *left*)

        world_x = camera.half_width - xoffset
        world_y = camera.half_height - yoffset

        # using the marea matrix, transform the canvas point and the origin,
        # and then compute the ray's direction vector
        # ( remember that the canvas is at z = -1 )

        pixel = camera.transform.inverse() * Point(world_x,world_y,-1)
        origin = camera.transform.inverse() * Point(0,0,0)


        # print("pixel:", type(pixel))
        # print("origin:", type(origin))
        # print("difference:", type(pixel - origin))
        
        direction = (pixel - origin).normalize()

        return Ray(origin,direction)
