# Сериализация (в программировании) — процесс перевода структуры данных в последовательность байтов.
#dump - encoded string writing on file
#dumps - encoding to JSON objects
#load - Decode while JSON file read
#loads - Decode the JSON string



import json


str_json = """{
 "update_id": 929428461,
 "message": {
  "message_id": 623499,
  "from": {
   "id": 956042390,
   "is_bot": false,
   "first_name": "Artem",
   "last_name": "Bla-bla",
   "username": "Art3k27",
   "language_code": "ru"
  },
  "chat": {
   "id": 956042390,
   "first_name": "Artem",
   "last_name": "Bla-bla",
   "username": "Art3k27",
   "type": "private"
  },
  "date": 1619300240,
  "text": "fg"
 }
}"""

data = json.loads(str_json)
print(data, "\n", type(data))
print(data['update_id'])
print()
for item in data['message']['from']:

    print(item)
    # можно удалять - del item['...']
    # или создать - item['likes'] = randint(100,200)

print()

new_json = json.dumps(data, indent=2)
print(new_json)

print()
print()

#with open('my.json', 'w') as file:
    #json.dump(data,file, indent=3) # создание файлика

with open('my.json','r') as file:
    data = json.load(file) # чтение из файлика

print(data, '\n', type(data))