# магические методы начинаються и заканчиваються с __

class Cat:

    def set_value(self, value, age = 0):
        self.name = value
        self.age = age

    def __init__(self, name, bread='pers', age=1, color='white'):
        print('hello new екземпляр' , self, name, bread,age,color) # визиваеться после создание обьекта
        self.name = name
        self.age = age
        self.bread = bread
        self.color = color                      # init нужен для инициализации

bob = Cat('Walt')
tom = Cat('Wolt')
bob.set_value('Bob')
print(tom.__dict__)
print(bob.__dict__)

print()

Cat('Tom','Siam',40,'black')

kelly = Cat('Kelly',age=40)

