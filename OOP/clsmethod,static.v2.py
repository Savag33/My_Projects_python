
# self - ссылаэться на екземпляр класса только
# cls - на сам класс


# если нам нужен метод, котрый бы работал с атрибутами экземпляра классов,
# то это однозначно обычний метод класса с первым параметром self, который указывает на текущий обьект.

# если на нужен метод, который можно вызивать непосредственно из класса или экземпляра и,
# который бы имел доступ к свойствам и методам этого класса , то его следует обьявить как метод класса через декоратор @classmethod

# если нужен метод, который можно вызивать непосредственно из класса, но доступ к его атрибутам не предпологається ,
# то достаточно его оюьявить как статический метод через декоратор @staticmethod

class Vector:

    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg): # in cls using Vector - class cls -> Vector
        if arg >= cls.MIN_COORD  and arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(x, y):
        return  x*x + y*y


    def __dict__(self):
        return print('its dict')

    def __repr__(self) -> str:
        return str(print('its dict'))


v = Vector()
print(Vector.validate(5))
print(Vector.norm2(1,2))

print(v.validate(101))
print(v.norm2(5,5))

print(v.__dict__)
