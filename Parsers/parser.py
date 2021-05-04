import requests
from bs4 import BeautifulSoup
import time


def check_currency():
    native = True

    while native:
        q = input("нажми 'q' для вихода или 'c' для продолжения")
        if q == 'q':
            native = False

        if q == 'c':
            GRN_DOLLAR = 'https://www.google.com/search?rlz=1C1AVFC_enUA877UA877&sxsrf=ALeKk01oCP0q7Fps6gLc7NXCrGOZxQTLyw:1602613051914&q=%D0%B3%D1%80%D0%BD+%D0%B2+%D0%B4%D0%BE%D0%BB&spell=1&sa=X&ved=2ahUKEwjlq6_tlrLsAhWP-ioKHdZsD5sQBSgAegQIDRAu&biw=1440&bih=757'

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

            full_page = requests.get(GRN_DOLLAR, headers=headers)

            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 3})

            print("Сейчас курс: 1 доллар = " + convert[0].text)
            time.sleep(1)
            check_currency()


check_currency()
