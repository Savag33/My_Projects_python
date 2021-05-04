
# dekorator
# декораторы нужны для разширения функционада функции


def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('/<h1>')

    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('/<table>')

    return inner

@header # say = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)

@table
def say_mom(name, surname, age):
    print('hello mom - ', name, surname, age)

say('Artem','Blazhenko',15)
print()
say_mom('Marian','loz',40)


print('-'*10)


def math(func):

    def inner(*args, **kwargs):
        print('Start calculate')
        func(*args,**kwargs)
        print('Finish calculate')

    return inner

@math
def math1(x):
    print(x**2)


math1(100)
