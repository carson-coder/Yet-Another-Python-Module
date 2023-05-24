from ..Other import RaisesError
import sys

# Huge thanks to fnky for https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797 which I uses alot for ansi codes


class Terminal():  # YAPM.Terminal.Terminal
    """
    A Class for more terminal customisation. Including printing with custom colors.

    :param bool TrueColor=True: Does this terminal support true color
    """
    ESC = "\033"
    RESET = ESC + "[0m"
    HOME = ESC + "[H"
    FORE_TRUE_COLOR = ESC + "[38;2;{};{};{}m"
    BACK_TRUE_COLOR = ESC + "[48;2;{};{};{}m"

    def __init__(self, TrueColor=True):
        self.TrueColor = TrueColor

    def __color__(self, color: tuple, fore: bool):
        return (self.FORE_TRUE_COLOR if fore else self.BACK_TRUE_COLOR).format(*color)

    def print(self, fore: tuple | None = None, back: tuple | None = None, *text, start_ansi: list[str] = [], end_ansi: list[str] = [], sep: str = " ", end: str = "\033[0m\n", **options):
        r"""
        Prints text with a given color

        :param Tuple[int 0-255 * 3] | None fore: The foreground of the text. White if None
        :param Tuple[int 0-255 * 3] | None back: The background of the text. Black if None
        :param \*str text: text to print, seperated by `sep`
        :param str start_ansi: Ansi codes to add before the text. Goes after the ansi color code. Automaticly adds ESC
        :param str end_ansi: Same as `start_ansi` but after the text. before `end`
        :param str sep=" ": The seperator to add between text
        :param str end="RESET\n": What to add at the end of the text. If changed add reset or text will stay colored
        :param str \**options: Options for the text. options are Bold, Italic, Strikethrough, Reverse, Underline, or Blinking. Goes before start_ansi.

        :returns: None
        :rasies ValueError: One or more of the arguments are the wrong type
        """
        if not RaisesError("int(color[2])", GlobalVars={"color": fore})[0]:
            raise ValueError("Fore should be a tuple with 3 ints")
        if not RaisesError("int(color[2])", GlobalVars={"color": back})[0]:
            raise ValueError("Back should be a tuple with 3 ints")
        elif not (print_text := RaisesError("map(str, text)", GlobalVars={"text": text}))[0]:
            raise ValueError("text has to be a list of str convertable stuff")
        elif not (start_text := RaisesError("map(str, text)", GlobalVars={"text": start_ansi}))[0]:
            raise ValueError("start_ansi has to be str convertable")
        elif not (end_text := RaisesError("map(str, text)", GlobalVars={"text": end_ansi}))[0]:
            raise ValueError("end_ansi has to be str convertable")
        elif not (sep := RaisesError("str(text)", GlobalVars={"text": sep}))[0]:
            raise ValueError("sep has to be str convertable")
        elif not (end := RaisesError("str(text)", GlobalVars={"text": end}))[0]:
            raise ValueError("end has to be str convertable")

        print_text = print_text[1]
        start_text = start_text[1]
        end_text = end_text[1]
        sep = sep[1]
        end = end[1]

        print_text = sep.join(print_text)
        print_text = self.__color__(fore, True) + self.__color__(back, False) + self.ESC.join(start_text) + print_text + self.ESC.join(end_text) + end

        sys.stdout.write(print_text)
