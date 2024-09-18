import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('qual produto você deseja? ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
  titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
  link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
  valor = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})

  print("titulo do iphone: ", titulo.text)
  print("Link do iphone: ", link['href'])
  if valor:
        preco = int(valor.text.replace('.', '')) 
        if preco < 5000:
            print("Preço do iPhone:", preco)
        else:
            print("Valor acima de 8000")
  print('\n\n')