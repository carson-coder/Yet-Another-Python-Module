from collections.abc import Sequence
from . import Random

#
# Adds a matrix class
# Used for math stuff.
#

# Multipling Rules
# x=y

class Matrix(): # 2d matrix
    def __init__(self, MatrixValues: Sequence[Sequence[int]]):
        if not Random.RaisesError("Matrix[0][0]", GlobalVars = {"Matrix": MatrixValues})[0]:
            raise ValueError("Matrix Values needs to be a Sequence[Sequence[int] (list[list[int]])")
        self.matrix = MatrixValues
    def __mul__(self, other):
        if not (Random.RaisesError("Matrix.matrix", GlobalVars = {"Matrix": other})[0] and len(self.matrix[0]) == len(other.matrix)):
            raise ValueError("X size of first matrix has to match Y value of second matrix. Or you arn't multiplying a matrix by a matrix or class that inheirts a matrix")
        
        MatrixValues = [[0]*len(other.matrix[0])]*len(other.matrix)
        
        for index, i in enumerate(self.matrix):
            values = [0] * len(other.matrix)
            for idx, b in enumerate(i):
                for idx2, k in enumerate(other.matrix[idx]):
                    values[idx2] += b * k
                    print(idx2, b, k)
            MatrixValues[index] = values
            print(values)
            
        return (Matrix(MatrixValues))