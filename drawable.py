from abc import abstractmethod

from context.context import Context


class Drawable:
    @abstractmethod
    def draw(self, context: Context) -> None:
        pass
