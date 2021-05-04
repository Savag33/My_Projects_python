#def rec(x):
    #print(x)  # рекурсия виполняет сама себ пока не будет виходп
    #rec(x+1)      или ограничения (просмотри)

                    #КОГДА ФУНКЦИЯ ВЫЗИВАЕТ САМА СЕБЯ

    #print(x)

#rec(1)




def rex(x):
    if x < 4:
        print(x)
        rex(x+1)
        print(x)

rex(1)
print()
def fac(x):
    if x==1:
        return 1
    return fac(x-1)*x

print(fac(5))


def fib(n):
    if n==1:
        return 0
    if n==2:                # fibonacii 0,1,2,3 (приплюсовивать)
        return 1
    return fib(n-1)+fib(n-2)

print(fib(5))




