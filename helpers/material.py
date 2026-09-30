from helpers.color import Color
class Material:
    def __init__(self,color : Color = Color(1,1,1), ambient : int | float = 0.1,diffuse : int | float =  0,specular : int | float = 0, shininess : int | float = 20):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __str__(self):
        return f"Material: \n Color-{self.color} \n Ambient-{self.ambient} \n Diffuse-{self.diffuse} \n Specular-{self.specular} \n Shininess-{self.shininess}"
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, Color):
            raise TypeError("color must be a Color")
        self._color = value
