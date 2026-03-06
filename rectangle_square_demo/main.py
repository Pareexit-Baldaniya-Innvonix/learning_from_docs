from classes.Rectangle import Rectangle
from classes.Square import Square

rectangle = Rectangle(2, 4)
assert rectangle.area == 8

square = Square(2)
assert square.area == 4

rectangle.resize(3, 5)
assert rectangle.area == 15

square.resize(3, 5)
print(f"Square area: {square.area}")

print("OK!")
