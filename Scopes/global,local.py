#  глобальная переменная  доступная в любом месте
# локальние доступние токо в пределах етого блока

name = 'Tom'
a = 5
N = (100,)


def myfunc(b):
    # global a
    a = 10
    for x in range(b):
        n = x + 1  # здесь a=10 как локальная переменная если написать global
        print(n, end=" ")  # мы будем работать с той которой создали в начале
        print()  # и если мы напишем принт(а) то будет уже 10
        # также можно писать глобал когда нет глобальной переменни
        # тоесть когда мы не обозначи а вообше


myfunc(6)
print()
print(a)


def say_hi():
    print('Hello', name)


def say_bye():
    name = 'Bob'
    print('Good bye', name)


say_hi()
say_bye()
print(name)

# nonlocal

x = 0


def outer():
    x = 1

    def inner():
        # nonlocal x
        x = 2
        print('inner:', x)
                        # каждая функция взяла свой х(переменную)

    inner()             # каторий обьявлен в своей области видимости
    print('outer:', x)


outer()
print('global:', x)

print()
print()

x1 = 0


def outer():
    x1 = 1

    def inner():
        nonlocal x1
        x1 = 2                # тоесть если мы напишем nonlocal
        print('inner:', x1)    # то  мы будем работать с x
                                # с уровнем выше с глоб так нельзя
    inner()
    print('outer:', x1)


outer()
print('global:', x1)

print()
print()

x2 = 0


def outer():

    global x2
    x2 = 1

    def inner():

        x2 = 2
        print('inner:', x2)
                                # вот что будет при global
    inner()
    print('outer:', x2)


outer()
print('global:', x2)
