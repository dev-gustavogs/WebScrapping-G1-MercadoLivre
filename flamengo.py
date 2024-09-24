import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('qual produto você deseja? ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'id':'ui-search-item__brand-discoverability ui-search-item__group__element'})

for produto in produtos:
    titulo = produto.find('h2', class_='ui-search-item__title ui-search-item__group__element')
    if titulo:
        print(titulo.text.strip())
