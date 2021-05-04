# IO - input,output(текстовий,бинарний)
# with,as в любом случае закривает файл,дает возможность обрабативать исключения(try)
# бинарние файли ето файли(все кроме текстових) ето аудие фото музика и тд... последовательность произвольных байтов,
# название связано с тем, что байты состоят из бит, то есть двоичных (англ. binary) цифр (0101010...)
# откривать можно только в 'wb','rb','ab' и тд
# bin(x) -> str x -- Целое число. Если x не является объектом int, следует определить для него метод __index__(), возвращающий целое.

import random
# работа с бинарними файлами
pic = 'download.jpg'
file = open(pic,'rb')

numbers = [1,2,3,45,6,7,8,9,0]

new_file = open('copy_' + pic, 'wb')
new_file.write(bytes(numbers))
new_file.write(file.read())  # зделало копию бинарного файла

file.close()
new_file.close()

new_file = open('copy_download.jpg','rb')
g = new_file.read(99)
print(g)
print()
print(bytes(g[2]))
new_file.close()

# теперь with,as (контекстний,менеджер), (можно орачивать в try,except)

with open('readme.txt','w') as f:
    f.write('hello world')  # зделало  файл  и добавила запись
    print()
    print(f)

with open('readme.txt','a') as f:
    f.write('\nworld hello')

print()

with open('readme.txt','r') as f:
    a = f.read()
    print(a)

print()
print()
# обработка ошибки Filenotfound
# подсчет строк (words)


filename = str(input('Your way'))

try:
    with open(filename) as f_obg:
        contents = f_obg.read()

except FileNotFoundError:
        msg = 'Sorry, the file' , '' , filename , '' , 'does not exist'
        print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print('The file' , filename , 'has about' , str(num_words) , 'words!')





