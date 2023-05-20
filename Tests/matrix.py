import YAPM
a = YAPM.Matrix.Matrix(
    [[1, 2, 3],
     [4, 2, 4]]
)

b = YAPM.Matrix.Matrix(
    [[9, 1],
     [4, 1],
     [3, 3]]
)

print((a * b))
