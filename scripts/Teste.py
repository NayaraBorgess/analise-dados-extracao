import os
import json

# Caminho do arquivo
CONFIG_PATH = os.path.join(os.getcwd(), 'config', 'config.json')

# Tente carregar o arquivo JSON
try:
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
    print("Arquivo JSON carregado com sucesso!")
    print(config)
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar o JSON: {e}")
except FileNotFoundError:
    print("Arquivo config.json não encontrado.")