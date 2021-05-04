# map (func , *iterables ) (iterables=dict,list,tuple,range,str...)

# make an iterator that computes the function
# using arguments from each of the iterables

def f(x):
    return x ** 2


a = [-1, -2, -3, 4, 5]

b = list(map(f, a))  # функция и потом переменная(функции-любиє  можно свои)
print(b)

print()

d = ['hello', 'hi', 'good morning']
c = list(map(str.upper, d))

print(c)

print()

v = list(map(lambda x: x[::-1], d))
print(v)

print()

g = list(map(lambda x: x+'!', d))
print(g)

print()                     # ето все можно зделать в генераторах списка

w = list(map(list, d))
print(w)

print()

h = list(map(sorted, w))
print(h)

print()

s = list(map(int, input().split()))
print(s)
