
import yaml
import os
import pandas as pd

# Ler config.yaml
def read_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

# Acessar valores
def get_config(config):
    diretorio = config["saida"]["diretorio"]
    data_inicio = config["periodo"]["data_inicio"]
    data_final = config["periodo"]["data_final"]
    codigo_empresa = config["empresa"]["codigo"]
    return diretorio, data_inicio, data_final, codigo_empresa

# Criar diretório se não existir
def create_directory(diretorio):
    os.makedirs(diretorio, exist_ok=True)

# baixando dados
def buscar_dados():
    dados = pd.read_parquet('historico.parquet', engine='pyarrow')

#salvando dados em parquet
def salvar_dados(dados, diretorio):
    dados.to_parquet(os.path.join(diretorio, 'historico_salvo.parquet'))
    return os.path.join(diretorio, 'historico_salvo.parquet')

def run():
    config = read_config()
    diretorio, data_inicio, data_final, codigo_empresa = get_config(config)
    create_directory(diretorio)
    dados = buscar_dados()
    caminho_arquivo = salvar_dados(dados, diretorio)
    print(f"Dados salvos em: {caminho_arquivo}")