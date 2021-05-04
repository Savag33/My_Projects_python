# split принадлежит к методом строки (из строки список)
# join принадлежит к списку (обьединяем список из елементов в одну строку)
a = '1,2,3,4,5,6'
s = 'Ivanov Ivan Ivanovich'
a2 = [40,54,32,65]
print(s.split())
print(s.split('I'))
print()

print(a.split(','))
c = input().split()
print(c)

print()

a1 = ['43','54','32','65']
print('&*'.join(a1))  # или преобрахить в строку через генератор списка

print('---'.join([str(i) for i in a2 ]))