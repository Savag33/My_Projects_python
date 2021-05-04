# name и age ето атрибути - Person.name
# __dict__ magit method - показивает все свойтва класса или еземпляра класса
# Person() - визов чего0то функции и тд
#
#
#
#
#
#
#

class Person:
    name = 'Ivan'
    age = 30



print(Person.age)
print(Person.name)
print(Person.__dict__)
print()

print(getattr(Person,'name')) # встроенная функция - дает доступ до атрибута
print(getattr(Person,'x',100)) # верняться 100 в случае если нету такого атрибута

print()

Person.name = 'Misha' # изменение
print(Person.name)
Person.x = [1,2,3]
print(Person.x)

print()

setattr(Person, 'x', 200) # установка атрибута
print(Person.x)
setattr(Person,'y',10) # или создание
print(Person.y)

print()

del Person.x
print(Person.__dict__)
delattr(Person,'y')
print(Person.__dict__)

print()

a = Person()  # екземпляр
print(a)
b = Person()
print(b)

print()

Person.z = 100
print(Person.__dict__)
print(a.age)
print(b.name)

print()

del Person.age # повлияэт на все екземпляри класса

a.hp = 200 # создание атрибута конкретно для екземпляра a
print(a.hp)
print(a.__dict__)
print(b.__dict__)
print(Person.__dict__)


