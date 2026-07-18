from helpers.matrix import Matrix
import math
class Transform:
    @staticmethod
    def identity():
        m = Matrix(4, 4)
        for i in range(4):
            m.mat[i][i] = 1
        return m
    @staticmethod
    def translation(x, y, z):
        m = Transform.identity()
        m.mat[0][3] = x
        m.mat[1][3] = y
        m.mat[2][3] = z
        return m

    @staticmethod
    def scaling(x, y, z):
        m = Transform.identity()
        m.mat[0][0] = x
        m.mat[1][1] = y
        m.mat[2][2] = z
        return m

    @staticmethod
    def reflection(x=False, y=False, z=False):
        m = Transform.identity()
        if x:
            m.mat[0][0] = -1
        if y:
            m.mat[1][1] = -1
        if z:
            m.mat[2][2] = -1
        return m
    
    @staticmethod
    def rotation_x(radians):
        m = Transform.identity()

        c = math.cos(radians)
        s = math.sin(radians)

        m.mat[1][1] = c
        m.mat[1][2] = -s
        m.mat[2][1] = s
        m.mat[2][2] = c

        return m


    @staticmethod
    def rotation_y(radians):
        m = Transform.identity()

        c = math.cos(radians)
        s = math.sin(radians)

        m.mat[0][0] = c
        m.mat[0][2] = s
        m.mat[2][0] = -s
        m.mat[2][2] = c
        
        return m

    @staticmethod
    def rotation_z(radians):
        m = Transform.identity()

        c = math.cos(radians)
        s = math.sin(radians)

        m.mat[0][0] = c
        m.mat[0][1] = -s
        m.mat[1][0] = s
        m.mat[1][1] = c
        
        return m

    @staticmethod
    def shearing(xy=0, xz=0,
                yx=0, yz=0,
                zx=0, zy=0):

        m = Transform.identity()

        m.mat[0][1] = xy
        m.mat[0][2] = xz

        m.mat[1][0] = yx
        m.mat[1][2] = yz

        m.mat[2][0] = zx
        m.mat[2][1] = zy

        return m