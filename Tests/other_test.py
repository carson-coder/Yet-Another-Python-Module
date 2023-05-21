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

from YAPM import Other


class Tests():
    def test_one(self):
        def is_list(a):
            result = Other.RaisesError("a[0]", GlobalVars={"a": a})
            if result[0]:
                return f"a[0] is {result[1]}"  # Result[1] is the return value
            else:
                return f"a[0] threw {result[1]}"  # Result[1] is the error.

        assert is_list([0, 1, 2]) == "a[0] is 0"
        assert is_list(1) == "a[0] threw 'int' object is not subscriptable"
