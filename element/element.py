from abc import abstractmethod

from element.bounding_box import BoundingBox
from element.drawable import Drawable
from primitives.point import Point


class Element(Drawable):
    @abstractmethod
    def drag(self, delta_point: Point) -> None:
        pass

    @abstractmethod
    def get_bounding_box(self) -> BoundingBox:
        pass
