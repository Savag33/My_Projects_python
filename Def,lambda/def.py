def hello():
    print("Get up ")
    print("Wake up ")
    print("Shut up ")

hello()

def square(x):
    print("Квадрат числа", x , "=" , x**2)

for i in range(1,11):
    square(i)

def multiply(a,b):
    print(a*b)

multiply(3,5)


def even(a):
    if a%2==0:
        print(a , "четное")
    else:
        print(a , "нечетное")
for i in range(1,21):
    even(i)

