.. _examples:

Examples
==========

Code Examples

-------------------------------------------------------------------------------

Matrix
-----------

Multiplying Matrices
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :caption: Create and multiply two matrices

  from YAPM import Matrix
  
  a = Matrix.Matrix(
    [[1, 2, 3],
    [4, 2, 4]]
  )

  b = Matrix.Matrix(
    [[9, 1],
    [4, 1],
    [3, 3]]
  )

  print((a * b)) # [[26, 12], [56, 18]]

Get Value From Matrix
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :caption: Get value from matrix at 2, 0

  from YAPM import Matrix

  a = Matrix.Matrix(
    [[1, 2, 3],
    [4, 2, 4]]
  ) 

  print(a.GetValue(2, 0) # 3

-------------------------------------------------------------------------------

Others
------

RaisesError
~~~~~~~~~~~
.. code-block:: python
  :caption: Try to get value from list and print if errored
  
  from YAPM import Other
  
  def is_list(a):
    result = Other.RaisesError("a[0]", GlobalVars={"a": a})
    if result[0]:
      print(f"a[0] is {result[1]}")  # Result[1] is the return value
    else:
      print(f"a[0] threw {result[1]}")  # Result[1] is the error.

  is_list([0, 1, 2])  # a[0] is 0
  is_list(1)  # a[0] threw 'int' object is not subscriptable
