import json

def get_username():
    filename = 'user1.json'
    try:
        with open(filename,encoding='utf-8') as f:
            user = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return user


def greet_user():

    username = get_username()
    if username:
        print('Мы вас запомним как: ' + username + " !")

    else:
        username = input('Введите ваше имя: ')
        filename = 'user1.json'
        with open(filename,'w',encoding='utf-8') as fl:
            json.dump(username,fl,ensure_ascii=False)
            print('Мы тебя запомним как: '  + username + " !")



greet_user()

