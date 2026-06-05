# Sistema de Estacionamento

Projeto desenvolvido para a disciplina de Banco de Dados.

## Descrição

Sistema de gerenciamento de estacionamento desenvolvido em Python integrado ao MySQL.

O sistema permite:

- Cadastro de clientes
- Cadastro de veículos
- Cadastro de vagas
- Controle de entrada e saída de veículos
- Controle de tickets
- Consulta de vagas livres
- Consulta de tickets abertos
- Relatório de faturamento

## Tecnologias Utilizadas

- Python 3
- MySQL
- MySQL Connector
- Visual Studio Code

## Estrutura do Projeto

### Modelagem

- Modelo Conceitual
- Modelo Lógico

### Banco de Dados

- Script DDL
- Views
- Functions
- Procedures
- Triggers
- Dados para teste

### Aplicação

- main.py
- cliente.py
- veiculo.py
- vaga.py
- ticket.py
- conexao.py

## Como Executar

### 1. Criar o banco de dados

A aplicação foi desenvolvida em Python e executada via terminal.

Não há executável (.exe) nem URL de hospedagem, pois o sistema é executado localmente através do arquivo:

python main.py.

Executar os scripts na seguinte ordem:

1. EstacionamentoLC.sql
2. EstacionamentoLCProgramacao.sql
3. EstacionamentoDadosTeste.sql

### 2. Instalar dependências

```bash
pip install -r requirements.txt
