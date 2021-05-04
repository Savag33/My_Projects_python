# filter(func, iterable)

def haso(string):               # filter возращает сначала True
    return 'o' in string.lower()

l = ['one','two','three','23Dsjk']

nl = list(filter(haso, l))
print(nl)

print()

newl = list(filter(lambda string: 'o' in string.lower(), l))

print(newl)

print()

#  а теперь с генератором списка

n12 = [string for string in l if haso(string)]
print(n12)

print()
print()
print()

# ZIP    (*iterables) обьединяет соответсвенние елементи упорядочных колекций
            # на виходе получаем итератор
a = [1,2,3,4,]
b = [5,6,7,8]
c = 'abracadabra'

it = list(zip(a,b,c))
print(next(it))


