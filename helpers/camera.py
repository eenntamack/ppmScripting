import math
from helpers.transformations import Transform
class Camera:
    def __init__(self,hsize: int | float = 160,vsize : int | float = 120,field_of_view : int | float = math.pi/2,transform: Transform = None):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = Transform.identity() if transform is None else transform
        half_view = math.tan(field_of_view/2)
        aspect_ratio = hsize/vsize

        if aspect_ratio >= 1:
            self.half_width = half_view
            self.half_height = half_view/aspect_ratio
        else:
            self.half_width = half_view * aspect_ratio
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2)/self.hsize



    @classmethod
    def default_camera(cls):
        hsize = 160
        vsize = 120
        field_of_view = math.pi/2
        transform = Transform.identity()
        return cls(
            hsize,
            vsize,
            field_of_view,
            transform
        )