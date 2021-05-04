from random import randint

for i in range(4) :      # i - ето перемення(любая)  а range - ето итерируемий обьект(есть строка список)
    print('inside',i)

print('outside',i)

for i1 in range(1,51):
    if i1%2==0 and i1%7==0:
        print(i1)

for a in range(1,11):
    print('Числа',a,'Квадрат',a**2)

# нахождения факториала как находится: надо найти факториал 5 тоесть 1*2*3*4*5=120

n = int(input(''))
pr = 1
for i in range(1,n+1):
    pr = pr * i
print(pr)

for i in range(5):
    s = randint(0,100)
    print(s,end=' ')
print()

s1=0
n1=int(input())
for i in range(n):
    s2=randint(1,10)
    s1+=s2
    print(s2,end=' ')
print()
print(s1)

n2=int(input())
s3=0
for i in range(n2):
    a1 = int(input())
    s3+=a1
    print('curent :s3 ',s3)
print('Total',s3)
print('Sred arif',s3/n2)

print('pause')
print('pause')
print('pause')










