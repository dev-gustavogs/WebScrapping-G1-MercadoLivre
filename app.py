import pandas as pd
import sqlite3
import streamlit as st

conn = sqlite3.connect('quotes.db')

#ler os dados do banco
df = pd.read_sql_query('SELECT  * FROM mercadolivre_items', conn)
conn.close()

st.title('Pesquisa de preços de tênis')
st.subheader('Teste')
st.write(df)