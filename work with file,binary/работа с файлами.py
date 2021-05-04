# уделения файла с помощью модуля os  - os.remove()
# encoding = тип кодировки кирилици
# r - убрать все екранирований символи
# режимы файла - 'r','w','a','a+'
# питон запоминает место где остановился
# r = открытие на чтение (является значением по умолчанию)
# 'w'= открытие на запись,(УДАЛЯЕТЬСЯ ТО ЧТО БЫЛО) содержимое файла удаляется, если файла не существует, создается новый.
# 'a'= открытие на дозапись, информация добавляется в конец файла.
# 't' = открытие в текстовом режиме (является значением по умолчанию).
# 'a+'	открытие на чтение и запись
# 'rb' - для чтения бинарних(двоичних) файлов
# “wb” - write-binary-mode соответственно(бинарних файлов)
# менеджеры контекста - Конструкция with ... as используется для оборачивания выполнения блока инструкций менеджером контекста
# или try,except,finally
# метод seek() - можно откатиться на любое место по цифре
# readline() - считает ожну строчку целиком
# readlines - врзрашает строки в список

file = open(r'C:\Users\blazh\OneDrive\Рабочий стол\virsh.txt', 'r', encoding='utf-8')

print(file.readline())
print('"')
print(file.read())
print()
file.seek(0)
print(file.read(19))
print()
print(file.read(19))
print()
file.seek(0)
s = file.readlines()
print(s)
file.close()
# for row in file:
# for letter in row:
# print(letter) по букве

# запись

file1 = open(r'C:\Users\blazh\OneDrive\Рабочий стол\virsh1.txt', 'w', encoding='utf-8')
file1.write('hello,\n')
file1.write('hello,\n')
file1.write('hello.\n')  # записалось
file1 = open(r'C:\Users\blazh\OneDrive\Рабочий стол\virsh1.txt', 'a+', encoding='utf-8')
file1.write('hi\n')
file1.close()


