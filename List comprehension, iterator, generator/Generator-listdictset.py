# [выражение for value in коллекция] выражения (i)-переменная
        # range тоже коллеция
import random
import os


b = [2 for i in range(7)]
print(b)

a = [i**2 for i in range(7)]
print(a)

a1 = [i*2 for i in 'heloo']
print()
print(a1)

print()

a2 = [random.randint(-10,10) for i in range(10)]
                        # ord - находит код елемента в таблице ascii
print(a2)

print()

b1 = [abs(elem) for elem in a2]
print(b1)

print()

b1 = [elem*2 for elem in b1]
print(b1)

print()
                    # [выражение for value in коллекция if условие]

b1 = [elem for elem in b1 if elem%2==0 and elem%3==0]

print(b1)

print()

w = input().split()
v = [int(i) for i in w]

print(v)

print()

n = int(input())
m = int(input())

s = [[1]*m for i in range(n)]
s[1][1] = 100

for i in s:
    print(i)

print()

d = [(i,j) for i in 'abc' for j in [1,2,3]]
print(d)

print()

d1 = [i*j for i in [2,3,4,5] for j in [1,2,3] if i*j>=10]
print(d1)

print()

# генератор множеств(сет) и dict{}

h = [9,8,7,4,5,6,3,2,1,5,5]

z = {x*2 for x in h}
print(z)

print()

y = {x: x*2 for x in h}            # x:-ключ   x*2 елемент ключа
print(y)

print()

                        # os.walk видает кортеж из трех елементов
                        # можна отрабативать целые диски
                       # path - работа с путями , join обьединяет пути


g = [ os.path.join(z,i)
      for z, x, c in os.walk('C:\\')
      for i in c if '.txt' in i]
print(g)                            # цикл проходить весь диск по условию
                                    # или без

