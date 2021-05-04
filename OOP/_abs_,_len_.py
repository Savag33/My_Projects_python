class Person:

    def __init__(self, name, surname, balance=1):
        self.name = name
        self.surname = surname
        self.balance = balance

    def __len__(self):
        return len(self.name + self.surname)


p = Person('Artem', 'Blantek')
print(p.__len__())
print(len(p))
print('-' * 10)


class Otrezok:
    def __init__(self, p1, p2):
        self.x1 = p1
        self.x2 = p2

    def __len__(self):
        print('called __len__')
        return abs(self)  # такая запись автоматом вызовет метод abs = self.__abs__()

    def __abs__(self):
        print('called __abs__')
        return abs(self.x2 - self.x1)


q = Otrezok(3, 10)

q1 = Otrezok(20, 10)

print(len(q))
print(len(q1))
