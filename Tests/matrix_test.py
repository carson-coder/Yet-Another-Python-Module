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

import YAPM


class Tests():
    def test_one(self):
        a = YAPM.Matrix.Matrix([[1, 2, 3],
                                [4, 2, 4]])

        b = YAPM.Matrix.Matrix([[9, 1],
                                [4, 1],
                                [3, 3]])

        assert (a * b).matrix == [[26, 12],
                                  [56, 18]]
