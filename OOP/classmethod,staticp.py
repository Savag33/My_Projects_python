# если нам нужен метод, котрый бы работал с атрибутами экземпляра классов,
# то это однозначно обычний метод класса с первым параметром self, который указывает на текущий обьект.

# если на нужен метод, который можно вызивать непосредственно из класса или экземпляра и,
# который бы имел доступ к свойствам и методам этого класса , то его следует обьявить как метод класса через декоратор @classmethod

# если нужен метод, который можно вызивать непосредственно из класса, но доступ к его атрибутам не предпологається ,
# то достаточно его оюьявить как статический метод через декоратор @staticmethod

class Example:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance hello {self}')

    @staticmethod
    def static_hello():
        """
        can be use with екзямляр and class
        :return:
        """
        print('static hello')

    @classmethod
    def class_hello(cls):
        print(f'instance hello {cls}')


b = Example()

print(b.static_hello())
print(Example.static_hello())
print()

c = Example()

print(c.class_hello())
print(Example.class_hello)
