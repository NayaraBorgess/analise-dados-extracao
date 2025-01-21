import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import uuid  # Importando o módulo uuid

# Configurações
fake = Faker('pt_BR')
random.seed(42)  # Para garantir que os dados sejam reproduzíveis

# Listas de nomes fictícios
vendedores = [fake.name() for _ in range(10)]
compradores = [fake.name() for _ in range(50)]
meios_pagamento = ['Cartão', 'Pix', 'Boleto', 'Dinheiro']

# Listas de produtos, códigos e segmentos
produtos = ['Smartphone', 'Notebook', 'TV 4K', 'Geladeira', 'Fogão', 'Máquina de Lavar', 'Câmera DSLR', 'Fone de Ouvido', 'Tablet', 'Micro-ondas']
codigos_produtos = [f'PROD{str(i).zfill(3)}' for i in range(1, 11)]  # PROD001, PROD002, ..., PROD010
segmentos_produtos = ['Eletrônicos', 'Eletrodomésticos', 'Informática', 'Áudio e Vídeo']

# Função para gerar uma data aleatória em 2023 no formato dia/mês/ano
def gerar_data():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%d/%m/%Y')  # Formato dia/mês/ano

# Gerando 1000 registros
dados = []
for _ in range(1000):  # Gerando 1000 registros
    quantidade = random.randint(1, 10)
    preco_unitario = round(random.uniform(10, 500), 2)
    valor_total = round(quantidade * preco_unitario, 2)
    
    # Escolhendo um produto, código e segmento aleatoriamente
    produto = random.choice(produtos)
    codigo_produto = codigos_produtos[produtos.index(produto)]
    segmento_produto = random.choice(segmentos_produtos)
    
    registro = {
        'id_venda': str(uuid.uuid4()),  # Gerando um UUID único para cada venda
        'data_venda': gerar_data(),  # Data no formato dia/mês/ano
        'nome_vendedor': random.choice(vendedores),
        'nome_comprador': random.choice(compradores),
        'meio_pagamento': random.choice(meios_pagamento),
        'quantidade': quantidade,
        'preco_unitario': preco_unitario,
        'valor_total': valor_total,
        'local_empresa': 'Belo Horizonte',
        'produto': produto,
        'codigo_produto': codigo_produto,
        'segmento_produto': segmento_produto
    }
    dados.append(registro)

# Criando um DataFrame
df = pd.DataFrame(dados)

# Salvando em um arquivo Excel
df.to_excel('vendas_belo_horizonte.xlsx', index=False)