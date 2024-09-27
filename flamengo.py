import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://ge.globo.com/futebol/times/flamengo/'

response = requests.get(url_base)

site = BeautifulSoup(response.text, 'html.parser')

noticias = site.findAll('div', attrs={'id':'bastian-feed-item'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'feed-post-body-title'})
    print(titulo.text)
    