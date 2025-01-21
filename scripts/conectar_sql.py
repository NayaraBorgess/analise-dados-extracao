from sqlalchemy import create_engine
import json

# Carregar configurações
with open('../config/config.json', 'r') as f:
    config = json.load(f)

# Conectar ao SQL Server
engine = create_engine(
    f"mssql+pyodbc://{config['sql_server']['usuario']}:{config['sql_server']['senha']}@"
    f"{config['sql_server']['servidor']}/{config['sql_server']['banco_de_dados']}?driver=ODBC+Driver+17+for+SQL+Server"
)

def get_connection():
    return engine.connect()