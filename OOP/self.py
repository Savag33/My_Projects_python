class Point:
    x = 1
    y = 1

    def setCoords(self):   # селф как минимум для синтаксиса питона
        print(self.__dict__) # он ссилаэться на екземпляр класса в нашем случчае(pt)

pt = Point()
pt.x = 5
pt.y = 10
pt.setCoords()

print()

class Point1:
    x = 1
    y = 1

    def __init__(self,x=0,y=0):
        print('Создание екземпляра класса') # конструктор инициализация класса(автомотически визиваесться при создании екземпляра)
        self.x = x
        self.y = y

     # def __del__(self):  # контроль удаления еэкземпляра
        # print('Удаление экземпляра: ' + self.__str__())  # деструктор - визиваеться когда екземпляр удаляється

    def setCoords1(self, x , y): # общий для всех екземпляров класса поинт1
        def __init__(self):
            print()

        self.a = x
        self.b = y

pt1 = Point1()
pt2 = Point1(5)
pt3 = Point1(5,10)
print()
pt1.setCoords1(5,10)
pt2.setCoords1(5,10)
pt3.setCoords1(5,10)

print(pt1.__dict__)
print(pt2.__dict__)
print(pt3.__dict__)





