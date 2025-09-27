# %%

import sqlite3
import pandas as pd

df = pd.read_parquet("historico.parquet", engine="pyarrow")

# criar e conectando ao banco

conexao = sqlite3.connect('Analise finaceiras.db')

# salvando dados no banco

df.to_sql('cotacoes', conexao, if_exists='replace', index=True)
conexao.commit()
print("Dados salvos no banco com sucesso")

#%%

consulta = pd.read_sql("SELECT * FROM cotacoes", conexao)
print(consulta.head())