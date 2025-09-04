# %%

import yfinance as yf
import pandas as pd


# Empresas ativas

def get_ativos():
    return ["AAPL", "PETR4.SA", "MSFT", "VALE3.SA", "GOOGL"]
ativos = get_ativos()

print("Ativos:", ativos)

# baixa preços da açções ativas

def get_historico(ativos):
    return yf.download(ativos, start="2023-01-01", end="2025-12-31")

dados = get_historico(ativos)

print("historico bruto", dados.head())

# salva a pesquisa em parquet

def salvar_dados_no_banco(dados):
    salvar = dados.to_parquet("historico.parquet")
salvar_dados_no_banco(dados)

print("Dados salvos no banco")