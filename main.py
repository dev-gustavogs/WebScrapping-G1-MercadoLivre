import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_csv('tenis.csv')

#setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino#D[A:tenis%20corrida%20masculino,L:undefined]"

df['_data_coleta'] = datetime.now()

#conectar ao banco de dados SQLite(ou criar um novo)
conn = sqlite3.connect('quotes.db')

#salvar o Dataframe no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

#fechar a conexão com o banco de dados 
conn.close()

print(df.head())