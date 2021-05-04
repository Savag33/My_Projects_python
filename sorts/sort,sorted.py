# sort метод списка а sorted встроенная функция
# sorted изменяет список а sorted временно - чтоб изменят
# надо воспользоваться методоом присваения a = sorted(a)


a = [4, -10, 43, -300, 54, 89, -34]
b = 'hello world'
c = ('hi', 'zero', 'abracadabra', 'picachu')

print(sorted(b))
print(sorted(c))  # временно

# ети функции можно делать и в сорт
print()

print(sorted(c, reverse=True))  # сортед всегда возращает список
print(sorted(a, reverse=True))

print()

# сортировка по ключам
# мы создали функцию soft которая нам возращала для нечет значение 1 а для чет 0
# сортировка по возрастанию индекса в списке а потом брала 1 и так же делала

#      a = 1 , 4 , 3, 6, 5, 2   и так поочереди ток сначала значение 0
# soft():  1   0   1  0  1  0      (начиная с 4)

a1 = [1, 4, 3, 6, 5, 2]


def soft(x):
    return x % 2


print(sorted(a1, key=soft))
print()


def soft1(x):
    if x % 2 == 0:
        return x
    else:
        return x + 100


print(sorted(a1, key=soft1))

# почему так получилось
#       a = 1,  4,  3,  6,  5,  2
# soft1:    101 4   103 6   105 2

print()

print(sorted(a1, key=lambda x: x % 2))
print()
l = ['Москва', 'Твер', 'Смоленск', 'Псков', 'Рязань']

print(sorted(l, key=lambda x: x[-1]))  # сортировка с конецной букви
print(sorted(l, key=lambda x: x[1]))  # с начальной букви

print()

l1 =[('eg', 'pyskin', 200),
    ('mymy', 'ic', 250),
    ('master i margarita', 'bulgakov', 500),
    ('mer dywu', 'gogol', 190)]



print(sorted(l1, key=lambda x: x[2])) # сортировка по цене индекс 2 означает 3 елемент в одном кортеже

