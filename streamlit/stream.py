
import streamlit as st
import yfinance as yf
import pandas as pd 


# Título do painel
def set_page_config():
    st.set_page_config(page_title="Painel de Ações", page_icon=":chart_with_upwards_trend:")
    st.title("Painel de Ações")
    st.markdown("""
        Este painel permite que você visualize o histórico de preços de ações.
        Digite o código da ação (ticker) e selecione o período para ver os dados.
    """)
    


# Entrada do usuário para escolher o ticker
def get_main(key = "ticker"):
    st.title("Painel de Ações")
    ticker= st.selectbox("Digite o código da ação:", ["PETR4.SA", "AAPL", "TSLA", "TODOS"], index=0)
    key= "ticker"
    return ticker


# Definir período
def get_periodo(key = "periodo"):
    periodo = st.selectbox("Selecione o período:", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"], index=5)
    key= "periodo"
    return periodo


#carregar dados do banco de dados para o gráfico

def carregar_dados(key = "carregar"):
    carregar = pd.read_parquet("historico.parquet")
    st.button("Carregar Dados")
    st.success("Dados carregados com sucesso!")
    key= "carregar"
    return carregar


# Chamar as funções para o painel e exibir o gráfico

def main():
    set_page_config()
    ticker = get_main()
    periodo = get_periodo()
    carregar = carregar_dados()

    if ticker and periodo:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=periodo)
        hist.to_parquet("historico.parquet")
        data = pd.read_parquet("historico.parquet")
        st.dataframe(data['Close'])
    else:
        st.warning("Por favor, selecione um ticker e um período.")

    
    
def run():
    main()
if __name__ == "__main__":
    run()
