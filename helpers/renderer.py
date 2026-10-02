from helpers.camera import Camera
from helpers.camera_folder.camera_operations import Cam_OPS
from helpers.world_folder.world_operations import ColorPixel
from helpers.world import World

class Render:
    @staticmethod
    def render(camera : Camera, world : World ):
        width = camera.hsize
        height = camera.vsize
        canvas = [
            [[0, 0, 0] for _ in range(width)]
            for _ in range(height)
        ]
        for y in range(height):
            for x in range(width):
                ray = Cam_OPS.ray_for_pixel(camera,x,y)
                # Convert Color 0-1+ → RGB 0-255
                color = ColorPixel.color_at(world, ray)
                r = max(0, min(1, color.r))
                g = max(0, min(1, color.g))
                b = max(0, min(1, color.b))

                canvas[y][x] = [
                    round(r * 255),
                    round(g * 255),
                    round(b * 255)
                ]
        return canvas


        