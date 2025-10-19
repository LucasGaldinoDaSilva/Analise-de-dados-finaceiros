# %%
import pandas as pd

# Função para carregar o arquivo Parquet
def carregar_dados(caminho_arquivo):
    """Lê um arquivo Parquet e retorna um DataFrame."""
    df = pd.read_parquet(caminho_arquivo)
    return pd.DataFrame(df)

# Função para calcular as estatísticas descritivas
def calcular_estatisticas(df):
    """Calcula valor máximo, mínimo, média e variação de cada coluna numérica."""
    valor_max = df.max()
    valor_min = df.min()
    media = df.mean()
    variacao = valor_max - valor_min

    # Cria um DataFrame com o resumo
    res = pd.DataFrame({
        'Máximo': valor_max,
        'Mínimo': valor_min,
        'Média': media,
        'Variação': variacao
    })

    return res

#  Função para exibir os resultados
def mostrar_resultados(resumo):
    """Exibe as estatísticas formatadas."""
    print(" Estatísticas Descritivas:")
    print(resumo)

# Função principal para rodar o processo completo
def main():
    caminho = 'historico.parquet'  # Caminho do arquivo
    df = carregar_dados(caminho)
    resumo = calcular_estatisticas(df)
    mostrar_resultados(resumo)

if __name__ == "__main__":
    main()
