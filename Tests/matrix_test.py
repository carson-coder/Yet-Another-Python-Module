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
