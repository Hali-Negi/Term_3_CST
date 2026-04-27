"""
This sample code demonstrates a design scenario where the Liskov Substitution Principle fails.

Liskov Substitution states Rectangle may be replaced by its child, Square, anywhere
Rectangle is used, without affecting program correctness

However, area() is written in a way that Square will not pass the assertion. Perhaps Square should
not inherit from Rectangle

Possible solution:
- Square should NOT be a child of Rectangle, but a separate class. With this design,
Square should not be passed into the area function, which only accepts Rectangles
"""

class Rectangle():
    def __init__(self):
        self._height = 0
        self._width = 0

    # Rectangle can have different values for width and height
    def set_width(self, width):
        self._width = width;

    # Rectangle can have different values for width and height
    def set_height(self, height):
        self._height = height;

    def area(self):
        return self._height * self._width

class Square(Rectangle):
    def __init__(self):
        super().__init__()

    #Square must have height and width be the same value
    def set_width(self, width):
        self._height = width
        self._width = width;

    # Squares must have height and width be the same value
    def set_height(self, height):
        self._height = height
        self._width = height;

# Simple unit test
# Fails liskov substitution principle because can't replace rectangle with square freely
def area(rectangle):
    rectangle.set_width(5)
    rectangle.set_height(2)
    print(rectangle.__class__.__name__, "height", rectangle._height, ", width", rectangle._width)
    print(rectangle.__class__.__name__, "area:", rectangle.area())
    assert (rectangle.area() == 10)


def main():
    rectangle = Rectangle()
    area(rectangle) #OK, will pass area assertion

    square = Square()
    area(square) #FAIL

if __name__ == '__main__':
    main()
