import math


class Shape:
    def area(self):
        raise NotImplementedError('Metoda powinna zostać wykorzystana w klasie dziedziczącej')

    def perimeter(self):
        raise NotImplementedError("Metoda powinna zostać wykorzystana w klasie dziedziczącej")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width * self.height


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b * self.c

    def perimeter(self):
        return 2 * (self.a + self.b + self.c)


circle = Circle(1)
print(f"Pole koła: {circle.area()}, Obwód koła: {circle.perimeter()}")

rectangle = Rectangle(1, 2)
print(f"Pole prostokąta: {rectangle.area()}, Obwód protokąta: {rectangle.perimeter()}")

triangle = Triangle(1, 2, 3)
print(f"Pole trójkąta: {triangle.area()}, Obwód trójkąta: {triangle.perimeter()}").
