from helpers.vector import Vector
from helpers.camera_folder.camera_operations import Cam_OPS

_from = Vector(1,3,2)
_to = Vector(4,-2,8)
_up = Vector(1,1,0)

t = Cam_OPS.view_transform(_from, _to, _up)
print(t)