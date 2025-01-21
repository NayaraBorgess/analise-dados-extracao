# Análise de Dados

Este projeto é destinado à análise de dados de vendas, com foco em Belo Horizonte. Ele inclui scripts para conectar a bancos de dados SQL, extrair e tratar dados, além de gerar relatórios de vendas.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

ANALISE-DADOS/
├── config/
│ └── config.json
├── dados/
│ └── vendas_belo_horizonte.csv
├── logs/
│ ├── log_20231001.txt
│ └── log_20250121.txt
├── scripts/
│ ├── conectar_sql.py
│ ├── extrair_tratar_dados.py
│ ├── arquivos_processados.txt
│ ├── gerar_vendas.py
│ └── Teste.py
├── README.md
└── requirements.txt

## Instalação

Para instalar as dependências necessárias, execute o seguinte comando:

bash
pip install -r requirements.txt 

## Uso
Conectar ao Banco de Dados SQL: Execute o script conectar_sql.py para estabelecer uma conexão com o banco de dados.

Extrair e Tratar Dados: Utilize o script extrair_tratar_dados.py para processar os dados brutos.

Gerar Relatórios de Vendas: O script gerar_vendas.py gera relatórios com base nos dados tratados.

## Logs
Os logs do projeto são armazenados na pasta logs/ e podem ser usados para monitorar a execução dos scripts.

## Contribuição
Se você deseja contribuir para este projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.