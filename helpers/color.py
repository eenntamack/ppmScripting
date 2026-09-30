from helpers.vector import Vector

class Color:
    def __init__(self, r=1, g=1, b=1):
        if r < 0 or g < 0 or b < 0:
            raise ValueError("Color components cannot be negative")
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        return Color(
            self.r + other.r,
            self.g + other.g,
            self.b + other.b
        )

    def __sub__(self, other):
        return Color(
            self.r - other.r,
            self.g - other.g,
            self.b - other.b
        )

    def __mul__(self, other):
        if isinstance(other, Color):
            return Color(
                self.r * other.r,
                self.g * other.g,
                self.b * other.b
            )

        if isinstance(other, (int, float)):
            return Color(
                self.r * other,
                self.g * other,
                self.b * other
            )
        return NotImplemented
    
    def __str__(self):
        return f"({self.r},{self.g},{self.b})"
    def __rmul__(self, other):
        return self * other