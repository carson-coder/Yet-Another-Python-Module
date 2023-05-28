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
        sys.stdout.write("Hello \x1b[48;2;23;60;162m\x1b[38;2;0;255;0mTest\x1b[0m\n")
        print(repr(cap))
        assert cap == "\x1b[48;2;23;60;162m\x1b[38;2;0;255;0mTest\x1b[0m\n"
    def test_two(self, capfd):
        term = Terminal.Terminal()
        term.print((255, 0, 0), (0, 0, 255), "Hello, World!", strike=True, bold=True)
        cap = capfd.readouterr().out
        output = "\x1b[48;2;0;0;255m\x1b[38;2;255;0;0m\x1b[1m\x1b[9mHello, World!\x1b[0m\n"
        sys.stdout.write(f"Hello {output}")
        print(repr(cap))
        assert cap == output
