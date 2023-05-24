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

from YAPM import Terminal


class Tests():
    def test_one(self, capfd):
        term = Terminal.Terminal()
        term.print((0, 255, 0), (23, 60, 162), "Test")
        cap = capfd.readouterr().out
        sys.stdout.write("Hello \033[38;2;0;255;0m\033[48;2;23;60;162mTest\033[0m\n")
        print(repr(cap))
        assert cap == "\033[38;2;0;255;0m\033[48;2;23;60;162mTest\033[0m\n"
