import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# setting path
sys.path = [parent, ]

from YAPM import Matrix


class Tests():
    def test_one(self):
        a = Matrix.Matrix([[1, 2, 3],
                           [4, 2, 4]])

        b = Matrix.Matrix([[9, 1],
                           [4, 1],
                           [3, 3]])

        assert (a * b).matrix == [[26, 12],
                                  [56, 18]]

    def test_two(self):
        a = Matrix.Matrix(
            [[1, 2, 3],
             [4, 2, 4]]
        )

        assert a.GetValue(2, 0) == 3
