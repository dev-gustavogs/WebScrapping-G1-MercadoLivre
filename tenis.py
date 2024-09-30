import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

url_base = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino#D[A:tenis%20corrida%20masculino,L:undefined]'

response = requests.get(url_base)

site = BeautifulSoup(response.text, 'html.parser')

produto = site.find('ol', attrs={'class': 'ui-search-layout ui-search-layout--grid'})

for produtos in produto:
  titulo = produtos.find('span', attrs={'class': 'ui-search-item__brand-discoverability ui-search-item__group__element'})
  descricao = produtos.find('a', attrs={'class' : 'ui-search-link__title-card ui-search-link'})
  preco = produtos.find('div', attrs = {'class' : 'ui-search-price__second-line'})
  lista_noticias.append([titulo.text, descricao.text, preco.text])
  print(titulo.text) 
  print(descricao.text)
  print(preco.text)
  
news = pd.DataFrame(lista_noticias, columns=['titulo', 'descricao', 'preco']) 
news.to_csv('tenis.csv', index=False, sep=";")
