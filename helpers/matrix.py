import random
from helpers.vector4 import Tuple

class Matrix:

    def __init__(self, rows, cols):

        self.rows = rows

        self.cols = cols

        self.mat = [[0 for _ in range(cols)] for _ in range(rows)]
    def matrixConstr(self, x, y):
        return [[1 for _ in range(x)] for _ in range(y)]
    def setRandomPoints(self,num):
        x = random.randint(0, self.cols - 1)
        y = random.randint(0, self.rows - 1)
        self.mat[y][x] = num

    def print(self, precision=4):
        for row in self.mat:
            print(" ".join(f"{v:.{precision}f}" for v in row))

    def __eq__(self, other, eps=1e-9):
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for y in range(self.rows):
            for x in range(self.cols):
                if abs(self.mat[y][x] - other.mat[y][x]) > eps:
                    return False
        return True
    
    def __mul__(self, other):
        # matrix * matrix
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Invalid matrix sizes")
            result = Matrix(self.rows, other.cols)
            for y in range(self.rows):
                for x in range(other.cols):
                    total = 0
                    for k in range(self.cols):
                        total += self.mat[y][k] * other.mat[k][x]
                    result.mat[y][x] = total
            return result
    # MATRIX * POINT/TUPLE
        if isinstance(other, Tuple):
            if self.cols != 4:
                raise ValueError("Transform matrix must be 4x4")
            x = self.mat[0][0]*other.x + self.mat[0][1]*other.y + self.mat[0][2]*other.z + self.mat[0][3]*other.w
            y = self.mat[1][0]*other.x + self.mat[1][1]*other.y + self.mat[1][2]*other.z + self.mat[1][3]*other.w
            z = self.mat[2][0]*other.x + self.mat[2][1]*other.y + self.mat[2][2]*other.z + self.mat[2][3]*other.w
            w = self.mat[3][0]*other.x + self.mat[3][1]*other.y + self.mat[3][2]*other.z + self.mat[3][3]*other.w
            return Tuple(x, y, z, w)
        
    def copy(self):
        m = Matrix(self.rows, self.cols)
        m.mat = [row[:] for row in self.mat]
        return m
    def _poinData(self, x, y):

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers")

        if x < 0 or y < 0:
            raise IndexError("Access must be within bounds 0-n")

        if x >= self.cols or y >= self.rows:
            raise IndexError("Point out of bounds")

        return self.mat[y][x]

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for y in range(self.rows):
            for x in range(self.cols):
                result.mat[x][y] = self.mat[y][x]
        return result

    def submatrix(self, row, col):
        result = Matrix(self.rows - 1, self.cols - 1)
        r2 = 0
        for y in range(self.rows):
            if y == row:
                continue
            c2 = 0
            for x in range(self.cols):
                if x == col:
                    continue
                result.mat[r2][c2] = self.mat[y][x]
                c2 += 1
            r2 += 1
        return result

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Must be square")
        if self.rows == 1:
            return self.mat[0][0]
        if self.rows == 2:
            return (
                self.mat[0][0] * self.mat[1][1]
                - self.mat[0][1] * self.mat[1][0]
            )
        total = 0
        for x in range(self.cols):
            sign = (-1) ** x
            total += sign * self.mat[0][x] * self.submatrix(0, x).determinant()
        return total

        # for x in range(self.dimX):
        #     sign = (-1) ** x
        #     minor = self.submatrix(0, x)
        #     total += sign * self.mat[0][x] * minor.determinant()

        # return total

            



    def minor(self, r, c):
        return self.submatrix(r, c).determinant()
        
    def cofactor(self, r, c):
        return ((-1) ** (r + c)) * self.submatrix(r, c).determinant()

    def isInvertable(m):
        if m.determinant() == 0:
            return False
        return True
    
    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix not invertible")
        cof = Matrix(self.rows, self.cols)
        for y in range(self.rows):
            for x in range(self.cols):
                cof.mat[y][x] = self.cofactor(y, x)
        adj = cof.transpose()
        inv = Matrix(self.rows, self.cols)
        for y in range(self.rows):
            for x in range(self.cols):
                inv.mat[y][x] = adj.mat[y][x] / det
        return inv
    
    def __str__(self):
        return f"({self.mat[0]},{self.mat[1]},{self.mat[2]},{self.mat[3]})"