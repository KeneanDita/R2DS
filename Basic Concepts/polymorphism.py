from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length **2

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

shapes = [circle(4), square(5), triangle(4,3), rectangle(5,7)]
for shape in shapes:
    print(f"{shape.area()} cm2")