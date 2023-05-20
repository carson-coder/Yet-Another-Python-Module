Examples
==========

Code Examples

-------------------------------------------------------------------------------

Matrix
-----------

Multiplying Matrices
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :caption: Create and multiply two matrices

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

Prints
  [[26, 12], [56, 18]]

Get Value From Matrix
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :caption: Get value from matrix at 2, 0

  import YAPM
  a = YAPM.Matrix.Matrix(
    [[1, 2, 3],
    [4, 2, 4]]
  ) 

  print(a.GetValue(2, 0)

Prints
  3
