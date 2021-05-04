#  else - В конструкции try/except есть опциональный блок else.
# Он выполняется в том случае, если не было исключения.
#
# Блок finally - это еще один опциональный блок в конструкции try.
# Он выполняется всегда, независимо от того, было ли исключение или нет.
# Сюда ставятся действия, которые надо выполнить в любом случае.
# Например, это может быть закрытие файла.
#  exception - пререхвативает все ошибки!
#
# можно писать пару() except
#
# МОЖНО ПРОВЕРЯТЬ САМИ ФУНКЦИИ
#
#
#
active = True
while active:
    try:
        a = input("Введите первое число: ")
        b = input("Введите второе число: ")
        print("Результат: ", int(a)/int(b))
        active = False
    except ValueError:
        print("Пожалуйста, вводите только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")

print()


try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Вот и сказочке конец, а кто слушал - молодец.")

print('-'*10)

def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('Handling')
    print('finish first')

def second():
    print('start second')
    1/0
    print('finish second')

first()


    
