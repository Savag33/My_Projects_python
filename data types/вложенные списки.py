a = [[0, 2, 4, 6], [1, 5, [4, 5, 7, 11], 9, 13], [3, 10, 17, 19]]

b = ['hello', 'hi', 'world']

print(len(a))
print(a[2][3])
print(a[0][1])
print(a[1][2][1])

print(b[2][-1])  # -1 последний елемент

print('pause')
print('pause')

a1 = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

for i in a1:
    for j in i:
        print(j, end=' ')
    print()

# обход по индексам
print()

for i in range(3):
    for j in range(4):
        print(a1[i][j], end=' ')
    print()
print(a1)

print()

for j in range(4):
    for i in range(3):
        print(a1[i][j], end=' ')
    print()
print(a1)

print()

for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a1[i][j], end=' ')
    print()

print()
print()

a2 = [[0, 2, 4, 6, ],
      [1, 5, 9, 13],
     [3, 10, 17, 19]
]

for i  in range(3):
    s=0
    for j in range(4):
        s+=a2[i][j]
    print(s)

print()

for j  in range(4):
    s=0
    for i in range(3):
        s+=a2[i][j]
    print(s)

print()

a3 = []

n=int(input()) # stroka
m=int(input()) # stolb
for i in range(n):
    a3.append([0]*m)
for i in a3:
    print(i)

print()

n1=int(input()) # stroka
m1=int(input()) # stolb
a4=[]

# сам создаеш список

for i in range(n1):
    b1=[]
    for i in range(m1):
        b1.append(int(input()))
    a4.append(b1)
for i in a4:
    print(i)




