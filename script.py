# %%
import yaml
import os
import pandas as pd

# Ler config.yaml
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Acessar valores
diretorio = config["saida"]["diretorio"]
data_inicio = config["periodo"]["data_inicio"]
data_final = config["periodo"]["data_final"]
codigo_empresa = config["empresa"]["codigo"]

# Criar diretório se não existir
os.makedirs(diretorio, exist_ok=True)

# baixando dados

dados = pd.read_parquet('historico.parquet', engine='pyarrow')

#salvando dados em parquet

dados.to_parquet(os.path.join(diretorio, 'historico_salvo.parquet'))


print(f"Arquivos serão salvos em: {diretorio}")
print(f"Período de análise: {data_inicio} até {data_final}")
print(f"Código da empresa: {codigo_empresa}")
