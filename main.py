# -*- coding: utf-8 -*-
import pip
try:
    import requests
except ModuleNotFoundError:
    print('Чел ты библотеку не поставил , я ее за тебя поставлю')
    pip.main(['install','requests'])
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print('Чел ты библотеку не поставил , я ее за тебя поставлю')
    pip.main(['install','bs4'])
try:
    from art import tprint
except ModuleNotFoundError:
    print('Чел ты библотеку не поставил , я ее за тебя поставлю')
    pip.main(['install','art'])


def parser_deanona(url):
    if requests.get(url).status_code == 404:
        print('Чел такой пасты не существует')

    else:
        siilka = requests.get(url)
        soup = BeautifulSoup(siilka.text,'html.parser')
        deanon = soup.find_all('div',class_='show-container')
        for text1 in deanon:
            print(text1.text)



if __name__ == '__main__':
    tprint('''
    DOXBIN PASTE 
    PARSER''', font="small",space=1)
    while True:
        name_pasta=input('Введите название пасты которые вы хотите получить (пустота -  остановка цикла) : ').replace('_','')
        name_pasta.replace(' ','')
        if name_pasta == '':
            print('Все я тебя понял , оставливаю процесс. ')
            break
        else:
            parser_deanona(f'https://doxbin.org/upload/{name_pasta}')
