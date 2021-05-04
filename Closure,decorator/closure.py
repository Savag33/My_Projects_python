# вот замыкание

def main_func(value):
    name = value
    def inner_func():
        print('hello my friend', name)

    return inner_func



d = main_func('Misha')
d()
print('-'*10)
v = main_func('Vasya')
v()


def adder(value):
    def inner(a):
        return value+a

    return inner

a2 = adder(2)

print(a2(8))
print(a2(5))
print('-'*3)


def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return  count
    return inner

q = counter()
q()
q()
print(q())
print(q())
print()
f = counter()
print(f())

