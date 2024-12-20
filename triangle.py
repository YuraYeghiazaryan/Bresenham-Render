from context.context import Context
from element.element import Element
from primitives.line import Line
from primitives.point import Point


class Triangle(Element):
    def __init__(self, angle1: Point, angle2: Point, angle3: Point):
        self.__angle1: Point = angle1
        self.__angle2: Point = angle2
        self.__angle3: Point = angle3

    def get_angle1(self) -> Point:
        return self.__angle1

    def get_angle2(self) -> Point:
        return self.__angle2

    def get_angle3(self) -> Point:
        return self.__angle3

    def draw(self, context: Context) -> None:
        for line in self.__to_lines():
            context.draw_line(line)

    def __to_lines(self) -> [Line]:
        return [
            Line(self.__angle1, self.__angle2),
            Line(self.__angle2, self.__angle3),
            Line(self.__angle3, self.__angle1),
        ]

    def drag(self):
        pass

    def get_area(self):
        pass