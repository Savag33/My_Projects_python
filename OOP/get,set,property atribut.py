# getter -  получает значение
# setter - устанавливает
import json


class BankAccount:

    def __init__(self, name, balance):
        self.fgbfsdgbdfgb = name
        self.__balance = balance

    def get_name(self):
        return self.fgbfsdgbdfgb

    # получает
    def get_balance(self):
        """
        Get a bank balance
        :return:
        """
        print('get balance')
        return self.__balance

    # УСТАНАВЛИВАЕТ
    def set_balance(self, value):
        """
        Set a value into bank balance
        :param value:
        :return:
        """
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Должно быть число')
        if value <= 0:
            raise ValueError('Value should be greatest then zero!')
        self.__balance = value

    def clear_balance(self):
        print('del balance')
        self.__balance = 0

    def calc_tax(self):
        """
        Calculate a tax for the current bank balance
        :return: balance * 0.2 (tax)
        """
        return float(self.__balance * 0.2)

    def __str__(self):
        return "Account name: " + self.name + " Balance: " + str(self.__balance) + " Tax: " + str(self.calc_tax())

    def __repr__(self) -> str:
        return self.__str__()

    # def __dict__(self):
    #     return {
    #         "name": self.fgbfsdgbdfgb,
    #         "balance": self.__balance,
    #         "tax": str(self.calc_tax())
    #     }

    balance = property(fget=get_balance,
                       fset=set_balance,
                       fdel=clear_balance)
    name = property(fget=get_name)


b = BankAccount('vasya', 100)

print(b.get_balance())
b.balance = 150
b.set_balance(400)
print(b.get_balance())
print(b.__dict__)
print()

d = BankAccount('Misha', 450)

print(d.balance)
d.balance = 666
print(d.balance)

print()

c = BankAccount('Vasa', 228)
print(c.balance)
del c.balance
print(c.name)
print(c.balance)
print(c)
print("The tax is " + str(c.calc_tax()))

print(json.dumps(c.__dict__))


data = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

for key, value in data.items():
    print(key + " = " + str(value))


