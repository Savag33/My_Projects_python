# тесты в testing.py
# middle='' - ето необязательний аргумент

def full_name(first,last, middle=''):

    """ Отдает полное имя и фамилию """

    if middle:
        full = first + ' ' + last + ' ' + middle
    else:
        full = first + ' ' + last
    return full.title()

