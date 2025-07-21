# 🏦 Meu Controle Financeiro v1.0

Este é um programa de console, desenvolvido em Python, para gerenciamento de finanças pessoais. Ele foi criado para registrar e analisar ganhos, despesas, dívidas, investimentos e metas financeiras, oferecendo uma visão clara da saúde financeira do usuário.

## ✨ Funcionalidades Implementadas (v1.0)

- [x] **Registro de Transações**: Adição de ganhos, despesas fixas, despesas variáveis, pagamentos de dívidas e aportes de investimentos.
- [x] **Resumo Mensal**: Geração de uma tabela consolidada com o balanço de cada mês.
- [x] **Controle de Orçamento**: Sistema de categorias de despesas com verificação de limites de gastos mensais.
- [x] **Calendário de Vencimentos**: Exibição de contas a pagar (pendentes) nos próximos 30 dias.
- [x] **Gerenciamento de Cartões**: Cadastro, listagem e exclusão de cartões de crédito.
- [x] **Mural dos Sonhos**: Cadastro de metas financeiras com cálculo automático de economia mensal necessária.
- [x] **Interface Interativa**: O programa é totalmente operado por um menu de console amigável.
- [x] **Persistência de Dados**: Todas as informações são salvas em arquivos `.csv` na pasta `data/`.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Para manipulação e análise de dados.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    # git clone URL_DO_SEU_REPOSITORIO
    ```
2.  **Crie e ative um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Mac/Linux:
    source venv/bin/activate
    ```
3.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o programa**:
    ```bash
    python src/financas.py
    ```

## ✅ Como Executar os Testes

1.  Certifique-se de ter instalado as dependências:
    ```bash
    pip install -r requirements.txt
    ```
2.  Rode o pytest na raiz do projeto:
    ```bash
    pytest
    ```

---
*Este projeto foi desenvolvido com a ajuda do Parceiro de Programação da Google.*
