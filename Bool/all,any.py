# любой обьект можна преоброзовать к логичискому типу(bool)
# пробегаеться по елементам и превращает в тру если не пучто и нету 0
c = ['','','world']
b = ['hello1','','world1']
a = ['hello','hi','world']
print(all(a))
print(any(a))
print()
print(all(b))
print(any(b))
print()
print(all(c))
print(any(c))
# ALL будет истина когда только в том когда в списке все елементи будут True
# ANY будет равна истине хотяб один елемент будет тру
# также с цифрами 0 ето фалсе
