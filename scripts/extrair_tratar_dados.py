import os
import pandas as pd
from sqlalchemy import create_engine
import json
from datetime import datetime

# Caminhos
PASTA_DADOS = os.path.join(os.getcwd(), 'dados')
ARQUIVOS_PROCESSADOS = os.path.join(os.getcwd(), 'arquivos_processados.txt')
CONFIG_PATH = os.path.join(os.getcwd(), 'config', 'config.json')
LOG_PATH = os.path.join(os.getcwd(), 'logs', f'log_{datetime.now().strftime("%Y%m%d")}.txt')

# Carregar configurações
try:
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
    print("Arquivo config.json carregado com sucesso!")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar o JSON: {e}")
    exit(1)
except FileNotFoundError:
    print("Arquivo config.json não encontrado.")
    exit(1)

# Conectar ao SQL Server (Windows Authentication)
if config['sql_server']['usuario'] == "" and config['sql_server']['senha'] == "":
    # Usar autenticação integrada (Windows Authentication)
    engine = create_engine(
        f"mssql+pyodbc://{config['sql_server']['servidor']}/{config['sql_server']['banco_de_dados']}?"
        f"trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    )
else:
    # Usar autenticação com usuário e senha
    engine = create_engine(
        f"mssql+pyodbc://{config['sql_server']['usuario']}:{config['sql_server']['senha']}@"
        f"{config['sql_server']['servidor']}/{config['sql_server']['banco_de_dados']}?driver=ODBC+Driver+17+for+SQL+Server"
    )

# Ler o nome da tabela do config.json
nome_tabela = config['nome_tabela']

# Ler lista de arquivos já processados
if os.path.exists(ARQUIVOS_PROCESSADOS):
    with open(ARQUIVOS_PROCESSADOS, 'r') as f:
        arquivos_processados_lista = f.read().splitlines()
else:
    arquivos_processados_lista = []

# Listar arquivos na pasta
arquivos = [os.path.join(PASTA_DADOS, arquivo) for arquivo in os.listdir(PASTA_DADOS) if arquivo.endswith('.csv')]

# Filtrar novos arquivos
novos_arquivos = [arquivo for arquivo in arquivos if arquivo not in arquivos_processados_lista]

if novos_arquivos:
    for arquivo in novos_arquivos:
        # Ler o arquivo CSV com ; como delimitador
        dados = pd.read_csv(arquivo, delimiter=';')

        # Verificar as colunas do DataFrame
        print("Colunas do DataFrame:", dados.columns)

        # Renomear colunas (se necessário)
        dados.columns = ['id_venda', 'data_venda', 'nome_vendedor', 'nome_comprador', 'meio_pagamento', 'quantidade', 'preco_unitario', 'valor_total', 'local_empresa', 'produto', 'codigo_produto', 'segmento_produto']

        # Tratar dados numéricos
        # Substituir vírgulas por pontos e converter para float
        dados['preco_unitario'] = dados['preco_unitario'].str.replace(',', '.').astype(float)
        dados['valor_total'] = dados['valor_total'].str.replace(',', '.').astype(float)

        # Converter quantidade para int
        dados['quantidade'] = dados['quantidade'].astype(int)

        # Verificar os tipos de dados após a conversão
        print("Tipos de dados após conversão:")
        print(dados.dtypes)

        # Inserir dados no SQL Server
        dados.to_sql(nome_tabela, con=engine, if_exists='append', index=False)

        # Atualizar lista de arquivos processados
        with open(ARQUIVOS_PROCESSADOS, 'a') as f:
            f.write(f"{arquivo}\n")

        # Registrar log
        with open(LOG_PATH, 'a') as f:
            f.write(f"{datetime.now()} - Arquivo processado: {arquivo}\n")

    print("Novos dados inseridos com sucesso no SQL Server!")
else:
    print("Nenhum novo arquivo para processar.")