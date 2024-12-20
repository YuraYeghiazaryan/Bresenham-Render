from primitives.point import Point


class BoundingBox:
    def __init__(self, point: Point, width: int, height: int):
        self.__point: Point = point
        self.__width = width
        self.__height = height

    def get_point(self) -> Point:
        return self.__point

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_right_top(self) -> Point:
        return Point(self.__point.x + self.__width, self.__point.y + self.__height)
