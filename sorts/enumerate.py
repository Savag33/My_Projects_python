a = [10,20,30,40,50,60]

print(enumerate(a))             # пронумерирует все обьекти
print(list(enumerate(a)))
                                # (функция)para  - делает пару р
print()                         # результат в кортеже

for para in enumerate(a):
    print(para)

print()
for index,value in enumerate(a):
    print(index,value)

print()

s = 'HELLO'

for index,value in enumerate(s):
    print(index,value)

print()

t = ('apple','banana','mango')

for index,value in enumerate(t):
    print(index,value)

print()

d = dict(a=1,b=2,c=3)

for index,value in enumerate(d):
    print(index,value)

print()

for index,value in enumerate(range(10,20)):
    print(index,value)

print()

for index,value in enumerate(t,10):
    print(index,value)

print()

for index,value in enumerate(a,100):
    print(index,value)


