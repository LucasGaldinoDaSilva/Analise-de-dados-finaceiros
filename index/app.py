
import pandas as pd
import plotly.express as px

def create_figure():
    df = pd.read_parquet('historico.parquet')
    fig = px.line(df, x='data', y='valor', title='Histórico de Valores')
    return fig

def main():
    fig = create_figure()
    fig.show()
if __name__ == "__main__":
    main()

