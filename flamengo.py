import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://ge.globo.com/futebol/times/flamengo/'

response = requests.get(url_base)

site = BeautifulSoup(response.text, 'html.parser')

noticias = site.find('div', attrs={'class':'feed-post bstn-item-shape type-materia'})

for noticia in noticias:
    titulos = noticias.find('a', attrs={'class': 'feed-post-link'})
    print(titulos.text)
    print(titulos['href'])
    subtitulo = noticias.find('div', attrs={'class': 'feed-post-body-resumo'})
    
    