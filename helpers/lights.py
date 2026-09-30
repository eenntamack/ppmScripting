
from helpers.color import Color
class PointLight:
    def __init__(self, position, intensity : Color):
        self.position = position
        self.intensity = intensity
    def __str__(self):
        return f"Position : {self.position} | Intensity : {self.intensity}  "


