answer = lambda x,y: x * y        # анонимная функция

print(answer(5,5))
print(answer('q',3))            # lambda можна не присваивать

print()

print((lambda x,y: x + y)(6,6))
print()

fun = lambda *args: args                      # если одна * то ето кортеж
                                    # если две ** то слова(key,value)
print(fun(2,56,78.56))

print()

fun1 = lambda **args: args
print(fun1(a=1,b=2,c=3))

print()

         # ламбда в условной операторе

f = lambda x:  'Like' if x > 100 else 'Subscribe'

print(f(101))

print()

d = lambda x: 'Like' if x > 100 else ('Subscribe 'if x > 0 else 'Folow Me')
print(d(-1))

