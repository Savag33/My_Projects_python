def average_numbers():
    numbers = []
    def inner(number):

        numbers.append(number)
        print(numbers)

        return sum(numbers) / len(numbers)
    return inner

a = average_numbers()
a(10)
a(2)
print(a(3))
print(a(15))
print('-'*10)

a1 = average_numbers()
print(a1(100))
print()



def add(a,b):
    return a+b

def mult(a,b,c):
    return a*b*c

def counter(func):
    count = 0

    def inner(*args,**kwargs):
        nonlocal count

        count +=1
        print(f"функция {func.__name__} вызывалась {count} раз")
        return func(*args, **kwargs)

    return inner

b = counter(add)
c = counter(mult)

print(b(200,300))
print(c(10,5,2))

b(100,1)
c(1,2,3)

