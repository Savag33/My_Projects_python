# - public - публичние данные
# _ - protected - нужно обозначать для програмиста что данный атрибут лучше не использовать вне класса
# __ - private - защищённие атрибуты
# dir - проверка атрибутов у екземпляра
class BankAccount:

    def __init__(self,name,balance,passport):
            self.__name = name
            self.__balance  = balance
            self.__passport = passport

    def print_public_data(self):
            self.__print_private_data()
    # def print_protected_data(self):
            # print(self._name, self._balance, self._passport)
    def __print_private_data(self):
            print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob',1000,24456768768)

account1.print_public_data()  # - инкапсуляция, доступ через метод
print()
#print(account1.__name)
#print(account1.__balance)
#print(account1.__passport)

print(dir(account1))

