# делегирование ето способ при котором в дочернем классе вы можете вызвать метод родительського класса

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'


    def breathe(self):
       print('human breathe')

class Doctor(Person):

    def __init__(self, name ,surname, age):
        super().__init__(name,surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname} {self.age}'


    def breathe(self):
        super().breathe()
        print('doctor breathe')



p = Person('Ivan','Ivanov')
d = Doctor('Petr','Petrov',25)
d.breathe()
print('-'*10)

print(p.name,p.surname)
print(d.name,d.surname,d.age)
print()
print(p)
print(d)

