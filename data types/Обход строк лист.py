a = [43,65,3,54,6]
#count=0
#for i in a:
    #print(i)
    #count+=1
    #print(count,'обход')
    #input()

#for i in a:
    #print(i,a.index(i))

#for i in range(5):
    #print(i,a[i])

#n=len(a)
#for i in range(n):
    #print(i,a[i])
    #a[i]+=5
#print(a)

a1=[1,2,3,4,32,4,5,3,5]
b=[]
for i in a1:
    if i not in b:
        b.append(i)
print(b)

s='Hello WOrld'
for i in s:
    if i>='a' and i <='z':
        print(i,'small')
    elif 'A'<=i<='Z':
        print(i,'Big')
    else:
        print(i)

vowels = 'aeiou'
c='aerrtutiujgfdkloi'
n=len(c)
for i in range(n-1):
    if c[i] in vowels and c[i+1] in vowels:
        print(c[i],c[i+1])



