# чисто каунтер, кайф  и кайфовыце функции

from collections import Counter

s = 'abrracadabra'
words = ['donald','mickey','donald','mickey','mickey']

letters = Counter(s)
names = Counter(words)

print(letters)
print(names)
print()
print(names['donald'])
print(names['mickey'])
print()
print(names.most_common())
print(letters.most_common(2))
print() # и нету ошибок  типов Keyerror

for i in names.elements():
    print(i)

print()
print(names.keys())
print()

r = Counter()
for i in [1,1,1,2,2,2,2,3,3]:
    r[i] += 1
print(r)
d = Counter([1,2,3,4])
print(d)
print()
