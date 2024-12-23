import os

from context.context import Context


class TerminalContext(Context):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def render(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

        for row in self._image:
            for color in row:
                pixel = '▊' if (color.r + color.g + color.b) / 3 > 128 else ' '
                print(pixel, end='')
            print('\n')
