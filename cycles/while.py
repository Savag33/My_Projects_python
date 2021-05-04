a = 10
while a > 1:
    print(a)
    a -= 1

print('pause')

i = 1
while i < 6:
  print(i)
  i += 1

print('pause')

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print('pause')

i = 1
while i < 6:

  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# алгоритм евклида для нахождения НОД - наибольшего общего делителя

a = int(input('num1'))
b = int(input('num2'))

while a!= b:
  if a>b:
    a=a-b
  else:
    b=b-a
print(a)

print('pause')

# инструкция continue перекидует в начало цикла а break виходит из цикла while True:  бесконечный цикл такой как 5>0 и тд

while True:
  a = input()
  if a == 'exit':
    break
  if len(a) < 5:
    continue
  print(a,len(a))

print('pause')

a = [34,65,2376,87,10] + [11,11]

for i in a:
  if i%2 == 0:
    print('yes')
  else:
    print('no')











