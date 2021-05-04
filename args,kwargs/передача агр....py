a, *b, c = [True, 7, 'hello', 9, '54', 67, 4, 3]  # можно делить по разному также можна строки кортежи и тд
print(a, b, c)
print()
a1, b1, *c1 = 'hello world'
print(a1, b1, c1)
print()
s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))  # работает как распакуватель
print()

def f(a, b, c, d):
    print(a, b, c, d)

a = ('hello',True,78,[3,4,5])
f(*a)
print()
                            # *args # имя может бить любое ГЛАВНОЕ СИМВОЛ * или **
def F (*args):    # может передавать сколько угодно неименованых аргументов
    s=0
    print(args)     # но они будут в виде кортежа
    for i in args:
        s+=i
    return s

print(F(1,2,3,4,5,6))

print()                        # *kwargs

def f1(**kwargs):       # можно передавать именование аргументи

        print(kwargs)            # в неограниченом количестве
                        # результат будет в словаре

print()

f1(a=1,b=5,c=6,name='tom')



def ff(**kwargs):                   # k,v  ето key,value - по ключу и значению
    for k,v in kwargs.items():
        print(k,v)

ff(a=5,b=8,c=98,name='art')


print()

def f2(*args,**kwargs):
    print(args,kwargs)

f2(5,4,3,5,7,7,a=10,b=18,d='hello')

print()

def outprint(*args,sep='#',end='@'):
    print(args,sep,end)

outprint(1,2,3,4,5,sep='90')
outprint(1,2)


