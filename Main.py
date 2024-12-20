import time

from container import Container
from context.impl.terminal_context import TerminalContext
from element.shapes.rectangle import Rectangle
from primitives.point import Point

context = TerminalContext(100, 15)
container = Container(context)

rectangle1 = Rectangle(Point(4, 6), 10, 3)
# rectangle2 = Rectangle(Point(5, 5), 10, 5)

container.add_element(rectangle1)
# container.add_element(rectangle2)

for i in range(0, 85):
    rectangle1.drag(Point(1, 0))
    # rectangle2.drag(Point(0, 0))
    container.render()
    time.sleep(0.1)

# container.render()