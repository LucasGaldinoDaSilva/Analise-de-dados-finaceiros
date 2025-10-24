import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go  


# Configuração da página

def set_page_config():
    st.set_page_config(page_title="Painel de Ações", page_icon=":chart_with_upwards_trend:")
    st.title("Painel de Ações")
    st.markdown("""
        Este painel permite que você visualize o histórico de preços de ações.
        Digite o código da ação (ticker) e selecione o período para ver os dados.
    """)


# Entrada do usuário

def get_ticker():
    ticker = st.selectbox(
        "Selecione o código da ação:",
        ["PETR4.SA", "AAPL", "TSLA"],
        index=0
    )
    return ticker

def get_periodo():
    periodo = st.selectbox(
        "Selecione o período:",
        ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"],
        index=5
    )
    return periodo


# Baixar e salvar dados

def baixar_dados(ticker, periodo):
    st.info(f"Baixando dados de {ticker}...")
    stock = yf.Ticker(ticker)
    hist = stock.history(period=periodo)

    if hist.empty:
        st.error("Nenhum dado encontrado. Verifique o código da ação.")
        return None

    hist.to_parquet("historico.parquet")
    st.success("Dados baixados e salvos com sucesso!")
    return hist


# Carregar dados do arquivo salvo

def carregar_dados():
    try:
        data = pd.read_parquet("historico.parquet")
        st.success("Dados carregados com sucesso!")
        return data
    except FileNotFoundError:
        st.warning("Arquivo 'historico.parquet' não encontrado. Baixe os dados primeiro.")
        return None


# Calcular estatísticas descritivas

def estatisticas_descritivas(df):
    valor_max = df['Close'].max()
    valor_min = df['Close'].min()
    media = df['Close'].mean()
    variacao = valor_max - valor_min

    resumo = pd.DataFrame({
        "Máximo": [valor_max],
        "Mínimo": [valor_min],
        "Média": [media],
        "Variação": [variacao]
    })
    return resumo


# Gráfico interativo com Plotly

def grafico_plotly(df, ticker):
    fig = go.Figure()

    # Linha de fechamento
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Close'],
        mode='lines',
        name='Preço de Fechamento',
        line=dict(color='royalblue', width=2)
    ))

    # Layout personalizado
    fig.update_layout(
        title=f"Evolução do Preço de Fechamento - {ticker}",
        xaxis_title="Data",
        yaxis_title="Preço (R$)",
        template="plotly_white",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)


# Função principal

def main():
    set_page_config()
    ticker = get_ticker()
    periodo = get_periodo()


    if st.button("Carregar Arquivo Local"):
        data = carregar_dados()
        if data is not None:
            st.subheader(f"Fechamento diário - {ticker}")
            st.dataframe(data[['Close']])

            st.subheader("📈 Gráfico Interativo (Plotly)")
            grafico_plotly(data, ticker)

            st.subheader("📊 Estatísticas Descritivas")
            st.dataframe(estatisticas_descritivas(data))


# Rodar o app

if __name__ == "__main__":
    main()
