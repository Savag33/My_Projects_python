# возращает из функции значения
def square1(x):
    print(x ** 2)


c = square1(6)
print(c)

print()

a = abs(-7)
b = max(4, abs(-90), 4, min(100, 200))
print(a)
print(b)

print()


def square(x):
    return x ** 2


d = square(6)  # также можно вложенно так square(square(3)) - 81
print(d)


def example():
    print(1)
    print(2)
    return 'hello'  # как только попадаете на return вы выходите из функции
    print(3)


example()

print()

print(example())


def even(x):
    if x % 2 == 0:
        return True
        # можно с елс
    return False


for i in range(1, 11):
    print(i, even(i))

print()


def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


for i in range(1, 8):
    print(i, factorial(i))

print()

def sochet(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(sochet(5,3))

def sqandper(a,b):
    mas = []
    mas.append(a*b)
    mas.append(2*(a+b))
    return mas

print(sqandper(3,6))

