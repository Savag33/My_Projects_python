# функция-генератор  yield
#   итенератор ето оператор (которий можно пройти одний раз) ... функция next()...
#


def genf():
    for i in [43, 65, 32]:
        yield i


g = genf()

print(next(g))
print(next(g))
print(next(g))



print()


def fact(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


s = fact(10)
print(next(s))
print(next(s))
print(next(s))          # таким образом економим память
                    # return вивел бы все в зараз( в списке)



