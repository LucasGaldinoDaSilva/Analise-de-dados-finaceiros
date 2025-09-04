# %%

import sqlite3

# criar e conectando ao banco 

conexao = sqlite3.connect("Analise financeiras.db")
cursor = conexao.cursor()

#criando tabela de usuario

cursor.execute("""
CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    setor TEXT
            )
""")

# tabela de historico de cotação

cursor.execute("""
CREATE TABLE IF NOT EXISTS cotacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER NOT NULL,
    data DATE NOT NULL,
    abertura REAL,
    fechamento REAL,
    maxima REAL,
    minima REAL,
    volume INTEGER,
    FOREIGN KEY (empresa_id) REFERENCES empresas (id),
    UNIQUE(empresa_id, data) -- evita duplicar cotações
)
""")

conexao.commit
print("Banco finaceiro criado com sucesso")