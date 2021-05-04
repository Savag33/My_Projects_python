a = [True,43,'hello',5.4,[3,4,5]]
b = []
w = [34, 435, 65, 768, 23, 7, 6]

# сцепление списков

a = a+[4]
a = ['hi'] + a

#  a = a*2 умнажения списка на скоко хочеш

print(a)
print(False in a,5.4 in a)
print(sum(w)) # также min max
print(sorted(w))
print (sorted(w,reverse=True))

print('pause')
print('pause')
print('pause')

e = [32,45,6,78,1,20,15]

print(e[-1])
print(e[1:4]) # правое число не берется

print(e[2:])
print(e[::2]) # с пошагом
print(e[2:6:2])

print(e[::-2])

e[0] = 100

print(e)

e[3:5] = 35,36
print(e)

del e[0]

print(e)








