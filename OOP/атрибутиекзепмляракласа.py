#
#
#
#
#


class Car:
    model = 'BMW'
    engine = 1.6

a1 = Car()
a2 = Car()

print(a2.engine)
print(a1.model)

print()

a1.seat = 4
print(a1.seat)
print(a1.__dict__)

print()

a1.model = 'Lada'
print(a1.model)
print(a1.__dict__)
print(Car.__dict__)

print()

a2.size = 80
print(a2.size)
print()
Car.r = 100
print(a2.r)
print(a1.r)
print(Car.r)

print()

print(a1.model)
del a1.model
print(a1.model) # если нет в самом екземпляре класса то ищем в самом классе





