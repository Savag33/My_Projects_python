a= list(range(5))
print(a)

b = list(range(10,20))
print(b)

c= list(range(1,100,10))
print(c)

d = list(range(10,0,-1))
print(d)

e = sum(range(1,101))
print(e)

q = len(range(5,15,5))
print(q)

a1,b1,c1 = range(5,8)
print(a1,b1,c1)

# итерируемый Обьект, предостовляючий возможность поочерёдного прохода по своим елементам

v = iter(range(5))
print(v)

print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))

n = iter([43,True,'hi'])
print(next(n))
print(next(n))
print(next(n))




