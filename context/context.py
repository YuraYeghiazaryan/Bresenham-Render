from abc import abstractmethod

from primitives.color import Color
from primitives.line import Line


class Context:
    def __init__(self, width, height):
        self._image = None
        self.__height = height
        self.__width = width
        self.clear()

    def clear(self):
        black = Color(0, 0, 0)
        self._image = [[black for _ in range(self.__width)] for _ in range(self.__height)]

    def set_pixel(self, x: int, y: int, color: Color) -> None:
        self._image[y][x] = color

    def draw_line(self, line: Line) -> None:
        x0 = line.point0.x
        x1 = line.point1.x
        y0 = line.point0.y
        y1 = line.point1.y
        dx = x1 - x0
        dy = y1 - y0
        step = max(abs(dx), abs(dy))
        if step != 0:
            step_x = dx / step
            step_y = dy / step
            for i in range(round(step) + 1):
                x = round(x0 + i * step_x)
                y = round(y0 + i * step_y)

                self.set_pixel(x, y, Color(255, 255, 255))

    @abstractmethod
    def render(self) -> None:
        pass
