from context.context import Context
from element.element import Element


class Container:
    def __init__(self, context: Context):
        self.__elements: [Element] = []
        self.__context: Context = context

    def add_element(self, element: Element):
        self.__elements.append(element)

    def render(self):
        self.__context.clear()

        for element in self.__elements:
            element.draw(self.__context)

        self.__context.render()
