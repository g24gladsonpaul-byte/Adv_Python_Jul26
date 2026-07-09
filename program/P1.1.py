#Abstract Base Class Example
from abc import ABC, abstractmethod

# Base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Child class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def description(self):
        return f"This shape has area {self.area():.2f}"


circle = Circle(5)
print(circle.area())
print(circle.perimeter())
print(circle.description())