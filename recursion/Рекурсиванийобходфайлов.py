import os
                                # os.listdir показывает содержимое по
                                 # указанному пути (НУЖЕН МОДУЛЬ OS)

                            # isdir проверяет на папку а isfile на файл
path = 'D:\\User'

print(os.listdir(path))
print()
for i in os.listdir(path):
    print(i,type(i),path+'\\'+i,os.path.isfile(path+'\\'+i))

print()
print()
print()

def obxodfile(path,level=1):
    print('Level=',level,'Content:',os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Спускаемся',path+'\\'+i)
            obxodfile(path+'\\'+i,level+1)
            print('Возращаемся в',path)
obxodfile(path)

print()
print()
print()












