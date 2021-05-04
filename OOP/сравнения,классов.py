# __eq__ = == self.x2 - self.x1
# __lt__ = <
# __le__ = <=
# __gt__ = >
# __ge__ = >=

# можно писать толлько один вид сравнений т.к обратка обработает также

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('call __eq__')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('call __lt__')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        print('called __le__')
        if isinstance(other, Rectangle):
            return self.area <= other.area
        elif isinstance(other, (int, float)):
            return self.area <= other


q = Rectangle(1, 2)
w = Rectangle(1, 2)
r = Rectangle(10, 2)

print(q == w)
print()
print(w == r)
print()
print(q < r)
print()
print(r < q)
print()
print(r > w)
print()
print(q<=w)
print()
print(r<=q)