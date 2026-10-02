from helpers.lights import PointLight
from helpers.point import Point
from helpers.vector import Vector
from helpers.lighting import Lighting
from helpers.color import Color
from helpers.material import Material
eyev = Vector(0,0,-1)
normalv = Vector(0,0,-1)
light = PointLight(Point(0,0,-10),Color(1,1,1))
in_shadow = True

result = Lighting.lighting(Material(),light,Point(0,0,0),eyev,normalv,in_shadow)
print(result)