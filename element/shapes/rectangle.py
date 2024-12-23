from context.context import Context
from element.bounding_box import BoundingBox
from element.element import Element
from primitives.line import Line
from primitives.point import Point


class Rectangle(Element):
    def __init__(self, top_left_point: Point, width: int, height: int):
        self.__top_left_point: Point = top_left_point
        self.__width: int = width
        self.__height: int = height

    def get_point(self) -> Point:
        return self.__top_left_point

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def draw(self, context: Context) -> None:
        for line in self.__to_lines():
            context.draw_line(
                line
            )

    def __to_lines(self) -> [Line]:
        x = self.__top_left_point.x
        y = self.__top_left_point.y
        width = self.__width
        height = self.__height

        return [
            Line(Point(x, y), Point(x + width, y)),
            Line(Point(x + width, y), Point(x + width, y + height)),
            Line(Point(x + width, y + height), Point(x, y + height)),
            Line(Point(x, y + height), Point(x, y))
        ]

    def drag(self, delta_point: Point) -> None:
        self.__top_left_point.x += delta_point.x
        self.__top_left_point.y += delta_point.y

    def get_bounding_box(self) -> BoundingBox:
        return BoundingBox(self.__top_left_point, self.__width, self.__height)
