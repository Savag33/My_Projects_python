# JSON - сохраняет, обрабативает, передачи(javascript object notation)
# json.dump() - для сохранения списков в файл  json
# json.load() - получает обьекти тоеcть считивает данные
# на писать ensure_ascii - для понятия кирилици и енкодинг

import json

nums = [2,657,43,98,1,0, False,'True']

filename = 'nums.json'


with open(filename, 'w') as f:
    json.dump(nums, f)

filename = 'nums.json'

with open(filename, 'r') as fl:
    nums_new = json.load(fl)
    print(nums_new)


print()
print()


filename1 = 'user.json'

try:
    with open(filename1) as f:
        user = json.load(f)
except:
    username = input('Введите ваше имя:')
    with open(filename1, 'w', encoding='utf-8') as fl:
        json.dump(username, fl, ensure_ascii=False)
        print('Мы вас запомним  как', username)

else:
    print( "Добро пожаловать " + user + '!')


