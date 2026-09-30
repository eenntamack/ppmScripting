import math

EPSILON = 1e-5

def approx_equal(a, b, epsilon=EPSILON):
    return abs(a - b) < epsilon

def clean_float(x, epsilon=1e-9):
    if abs(x) < epsilon:
        return 0.0
    return x
class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def magnitude(self):

        return math.sqrt(

            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2 +
            self.w ** 2

        )

    def normalize(self):
        mag = math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return self.__class__(
            self.x / mag,
            self.y / mag,
            self.z / mag
        )
    
    def __mul__(self, scalar):

        return self.__class__(

            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar
            
        )
    
    def __add__(self, other):
        return self.__class__(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )
    def print(self):
        x = self.x
        y = self.y
        z = self.z

        print(f"({x},{y},{z})")
    def __sub__(self,other):
        return self.__class__(
            clean_float(self.x - other.x),
            clean_float(self.y - other.y),
            clean_float(self.z - other.z),
            clean_float(self.w - other.w)

        )
    def dot(self, other):
        return clean_float(self.x*other.x + self.y*other.y + self.z*other.z)
    
    def tmulm (self,other):

            
        x = other.mat[0][0] * self.x + other.mat[0][1] * self.y + other.mat[0][2] * self.z + other.mat[0][3] * self.w 
        y = other.mat[1][0] * self.x + other.mat[1][1] * self.y + other.mat[1][2] * self.z + other.mat[1][3] * self.w 
        z = other.mat[2][0] * self.x + other.mat[2][1] * self.y + other.mat[2][2] * self.z + other.mat[2][3] * self.w 
        w = other.mat[3][0] * self.x + other.mat[3][1] * self.y + other.mat[3][2] * self.z + other.mat[3][3] * self.w 

        return self.__class__(
            x,
            y,
            z,
            w
        )