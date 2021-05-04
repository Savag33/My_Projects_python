

# тестирование функции

from full_name import full_name

print('Для остановки теста введите символ  "q" ')
while True:
    first = input('\nВведите свое имя ')
    if first == 'q':
        break
    last = input('\nВведите вашу фамилию ')
    if last == 'q':
        break
    format_name = full_name(first,last)
    print('\nФорматирование имени: ' + format_name)


