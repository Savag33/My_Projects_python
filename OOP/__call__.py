from time import perf_counter


class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывалась функция  {self.fn.__name__} ')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 2
    return fib(n - 1) + fib(n - 2)

print(fact)
print(fact(6))

print()

Timer(fib)(7) # если обычно задекорируем тогда будет рекурсия fib = Timer(fib)
